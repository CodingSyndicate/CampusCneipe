{ sources ? import ./sources.nix
, pkgs ? import sources.nixpkgs {}
}:

let
  python-with-my-packages = pkgs.python3.withPackages (p: with p; [
    requests
  ]);
in {
  c2_pkgs = [
    # c2 website
    python-with-my-packages
    pkgs.nodejs
    pkgs.nodePackages.npm
    # nix dependency management
    pkgs.niv
    # for docker image / gitlab CI
    pkgs.gnutar
    pkgs.coreutils
    pkgs.bash
    pkgs.git
    pkgs.cacert
    pkgs.gnugrep
    pkgs.openssh
    pkgs.sshpass
    pkgs.gzip
    pkgs.rsync
    pkgs.curl
    pkgs.gnused
  ];
}
