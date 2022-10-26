{ sources ? import ./sources.nix
, pkgs ? import sources.nixpkgs {}
}:
let
  #from https://github.com/smarkets/marge-bot/blob/d3c440966f9bc3f41d82e65f58850e8609e17e5d/dockerize.nix
  basicShadow =
    # minimal user setup, so ssh won't whine 'No user exists for uid 0'
    pkgs.runCommand "basic-shadow-setup" {}
      ''
        mkdir -p $out
        cd $out
        mkdir -p root/.ssh
        mkdir -p etc/pam.d
        echo "root:x:0:0::/root:/bin/sh" >etc/passwd
        echo "root:!x:::::::" >etc/shadow
        echo "root:x:0:" >etc/group
        echo "root:x::" >etc/gshadow
        cat >etc/pam.d/other <<\EOF
        account sufficient pam_unix.so
        auth sufficient pam_rootok.so
        password requisite pam_unix.so nullok sha512
        session required pam_unix.so
        EOF
      '';
in
pkgs.dockerTools.buildLayeredImage {
  name = "c2-website-builder";
  tag = "latest";
  created = "now";

  contents = [ basicShadow ] ++ (import ./c2_pkgs.nix {}).c2_pkgs;

  extraCommands = ''
    mkdir -p usr/bin
    ln -sf ${pkgs.coreutils}/bin/env usr/bin/env
    mkdir tmp
    chmod 1777 tmp
  '';
  
  config = {
    Cmd = [ "/bin/bash" ];
    WorkingDir = "/";
    Env = [
      "SSL_CERT_FILE=/etc/ssl/certs/ca-bundle.crt"
    ];
    ## needed for container/host resolution
    nsswitch-conf = pkgs.writeTextFile {
      name = "nsswitch.conf";
      text = "hosts: dns files";
      destination = "/etc/nsswitch.conf";
    };
  };
}
