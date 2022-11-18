{ sources ? import ./sources.nix
, pkgs ? import sources.nixpkgs {}
}:

let
  python-with-my-packages = pkgs.python39.withPackages (p: with p; [
    requests
    google-auth
    google-api-python-client
    google-auth-httplib2
    google-auth-oauthlib
    GitPython
    chevron
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
