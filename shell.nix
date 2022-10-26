# shell.nix
#{ pkgs ? import <nixpkgs> {} }:
{ sources ? import ./nix/sources.nix
, pkgs ? import sources.nixpkgs {}
}:

pkgs.mkShell {
  buildInputs = [
    (import ./nix/c2_pkgs.nix {}).c2_pkgs
  ];
}
