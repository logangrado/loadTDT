# Changelog

## [0.6.2] - 2019-09-05
### Fixed
- Fixed error where SEV reader failed to parse store name in edge case

## [0.6.1] - 2019-08-30
### Changed
- `read_stores()` no longer re-loads stores that have already been read.
  - New optional argument `reload` can be used to force re-loading

## [0.6.0] - 2019-08-30
### Added
- Added SEV file reader

## [0.5.2] - 2019-08-26
### Changed
- Improved documentation

## [0.5.1] - 2019-08-26
### Fixed
- Fixed bug encountered when reading blocknotes

## [0.5.0] - 2019-08-09
### Changed
- Changed package name from `tdt` to `pytdt`

## [0.4.0] - 2018-12-12
### Added
- Added support for epochs
