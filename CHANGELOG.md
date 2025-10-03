# Changelog

## [0.10.6](https://github.com/sb-icon/icon-governance/compare/v0.10.5...v0.10.6) (2025-02-03)


### Bug Fixes

* add preps indexes ([3c06114](https://github.com/sb-icon/icon-governance/commit/3c06114647877e193983ee11c4584d4e8de44065))
* make more fixes from sqla + fastapi updates ([228679c](https://github.com/sb-icon/icon-governance/commit/228679c13a93b0993d34dbb4fff2979f5134eef2))
* rm echo in db and add pool ([8a2b0bc](https://github.com/sb-icon/icon-governance/commit/8a2b0bc69cff04a326cc18b0ae2930dbdead6f31))
* updated bond_percent formula [#60](https://github.com/sb-icon/icon-governance/issues/60) ([8d0e583](https://github.com/sb-icon/icon-governance/commit/8d0e583eab1f9472c9893f7344238ae36147fb87))

## [0.10.5](https://github.com/sb-icon/icon-governance/compare/v0.10.4...v0.10.5) (2024-10-14)


### Bug Fixes

* ci runner image version ([79e9626](https://github.com/sb-icon/icon-governance/commit/79e9626f4b191266e2a3ec86ae801525558aeef9))

## [0.10.4](https://github.com/sb-icon/icon-governance/compare/v0.10.3...v0.10.4) (2024-10-11)


### Bug Fixes

* capitalise router tags ([994a260](https://github.com/sb-icon/icon-governance/commit/994a260770bf69af18a6c27c7ad1c56e1be25038))

## [0.10.3](https://github.com/sb-icon/icon-governance/compare/v0.10.2...v0.10.3) (2024-10-06)


### Bug Fixes

* cps test ([eff79b8](https://github.com/sb-icon/icon-governance/commit/eff79b89718a4c2f0262cf5fdebd578866ca8177))

## [0.10.2](https://github.com/sb-icon/icon-governance/compare/v0.10.1...v0.10.2) (2024-10-06)


### Bug Fixes

* add tags to fastapi router and fix function names ([be6875c](https://github.com/sb-icon/icon-governance/commit/be6875c318a5d3bef0c1221a988dbdf5fcec9a0c))

## [0.10.1](https://github.com/sb-icon/icon-governance/compare/v0.10.0...v0.10.1) (2024-09-04)


### Bug Fixes

* rm code cov in ci ([ad0be77](https://github.com/sb-icon/icon-governance/commit/ad0be77c45cbe060d1206f45d65d802e677fa746))

## [0.10.0](https://github.com/sb-icon/icon-governance/compare/v0.9.0...v0.10.0) (2024-09-03)


### Features

* update bondRequirementRate per rev28 for mainnet ([bae3878](https://github.com/sb-icon/icon-governance/commit/bae387845a3e12b4a623ea3a07ebe36bef4ae3b1))


### Bug Fixes

* apy_time endpoint - limit to 100 due to timeout ([f620f0b](https://github.com/sb-icon/icon-governance/commit/f620f0b9aaa745315203b9be0965ec767ef2cd3c))
* release ([475bf59](https://github.com/sb-icon/icon-governance/commit/475bf5970d63999ebeddbad24b3e4dca1048ff35))

## [0.9.0](https://github.com/sb-icon/icon-governance/compare/v0.8.1...v0.9.0) (2024-08-14)


### Features

* add sort on preps endpoint [#44](https://github.com/sb-icon/icon-governance/issues/44) ([16ffd87](https://github.com/sb-icon/icon-governance/commit/16ffd871a0ce8f71994b67f0bce737b43cc3c459))


### Bug Fixes

* recalculate bond % with new bond requirment rate ([acc78b6](https://github.com/sb-icon/icon-governance/commit/acc78b69a3d6039b31c644225f457b35dac5a745))

## [0.8.1](https://github.com/sb-icon/icon-governance/compare/v0.8.0...v0.8.1) (2024-04-02)


### Bug Fixes

* add some extra try except around db conns [#42](https://github.com/sb-icon/icon-governance/issues/42) ([b2f4fa0](https://github.com/sb-icon/icon-governance/commit/b2f4fa0d21a32cafe7ba56731114cd4056da3c35))
* make apy column nullable ([a890e17](https://github.com/sb-icon/icon-governance/commit/a890e1730840725c44a4ae36e70f815a4ee64a66))

## [0.8.0](https://github.com/sb-icon/icon-governance/compare/v0.7.6...v0.8.0) (2024-03-23)


### Features

* add commission time stats ([5625dad](https://github.com/sb-icon/icon-governance/commit/5625dad4417875c2a9e7eea1356bb41be7eb88b6))


### Bug Fixes

* update apy time with average commission rate for iiss4 ([a7dbf37](https://github.com/sb-icon/icon-governance/commit/a7dbf375f9c5c5def79a15251ba57e81fbc8fda0))
* wage with default in table ([842a0d3](https://github.com/sb-icon/icon-governance/commit/842a0d383c1c8eaf8c6ccb29b8dc6e03c322efd1))

## [0.7.6](https://github.com/sb-icon/icon-governance/compare/v0.7.5...v0.7.6) (2024-03-11)


### Bug Fixes

* wage calculation ([4307639](https://github.com/sb-icon/icon-governance/commit/43076398d7caaa858da4aa75e8ab98b505ea36c0))
* wage calculation again ([339c39f](https://github.com/sb-icon/icon-governance/commit/339c39f65a15d880d49ad516f87409eadbf6557c))

## [0.7.5](https://github.com/sb-icon/icon-governance/compare/v0.7.4...v0.7.5) (2024-02-04)


### Bug Fixes

* flakey iiss test ([bc4f42b](https://github.com/sb-icon/icon-governance/commit/bc4f42b9ddaafb71b137b18990a50d34b10783ce))

## [0.7.4](https://github.com/sb-icon/icon-governance/compare/v0.7.3...v0.7.4) (2024-02-02)


### Bug Fixes

* conditional on jail flag for rewards ([19dda0b](https://github.com/sb-icon/icon-governance/commit/19dda0b021d28bb36f0bd693df6049c3ed527762))

## [0.7.3](https://github.com/sb-icon/icon-governance/compare/v0.7.2...v0.7.3) (2024-02-02)


### Bug Fixes

* issue with rev 24/25 missing iwage data ([7ab5a01](https://github.com/sb-icon/icon-governance/commit/7ab5a01fbc717e1b7b671c1a77fa721c6aa92916))

## [0.7.2](https://github.com/sb-icon/icon-governance/compare/v0.7.1...v0.7.2) (2024-02-01)


### Bug Fixes

* update ci to release main ([5d23e8a](https://github.com/sb-icon/icon-governance/commit/5d23e8a715afc297c054e0a9c50162fcbad6d69a))

## [0.7.1](https://github.com/sb-icon/icon-governance/compare/v0.7.0...v0.7.1) (2024-01-24)


### Bug Fixes

* cps methods from updated contract closes[#30](https://github.com/sb-icon/icon-governance/issues/30) ([9d10e30](https://github.com/sb-icon/icon-governance/commit/9d10e3050b1074b188e5f9c355297c07d7571d5a))
* update rewards per iiss4 ([664bae0](https://github.com/sb-icon/icon-governance/commit/664bae0bf1a3feaa5dcccc97aca8fee9b0b4ae61))

## [0.7.0](https://github.com/sb-icon/icon-governance/compare/v0.6.0...v0.7.0) (2023-12-27)


### Features

* implement iiss 4.0 attributes [#32](https://github.com/sb-icon/icon-governance/issues/32) ([ccc6822](https://github.com/sb-icon/icon-governance/commit/ccc682264801f167872759be83403bebc6a852a6))

## [0.6.0](https://github.com/sb-icon/icon-governance/compare/v0.5.2...v0.6.0) (2023-12-08)


### Features

* add apy over time endpoint ([b5a170b](https://github.com/sb-icon/icon-governance/commit/b5a170bd3831023a32d9313f03b0643004b8910b))
* add bonders and stakers counts to preps and stats table with total delegators [#29](https://github.com/sb-icon/icon-governance/issues/29) [#27](https://github.com/sb-icon/icon-governance/issues/27) ([725c550](https://github.com/sb-icon/icon-governance/commit/725c5507114289ad6ed513c3efa6068653e38208))


### Bug Fixes

* apy time crashing in testnets - start block does not exist [#31](https://github.com/sb-icon/icon-governance/issues/31) ([608f12f](https://github.com/sb-icon/icon-governance/commit/608f12f4ced8179cca8ee04bb13e246e0338f2c5))

## [0.5.2](https://github.com/sb-icon/icon-governance/compare/v0.5.1...v0.5.2) (2023-11-05)


### Bug Fixes

* add User-Agent header to details pull in preps_base [#23](https://github.com/sb-icon/icon-governance/issues/23) ([920d26c](https://github.com/sb-icon/icon-governance/commit/920d26c8f86e6143920aec810e7318e5fdd1379a))

## [0.5.1](https://github.com/sb-icon/icon-governance/compare/v0.5.0...v0.5.1) (2023-09-17)


### Bug Fixes

* public key insert in db ([4d7ed5e](https://github.com/sb-icon/icon-governance/commit/4d7ed5eb1fc6927899749e0f7b0bd5b950af1a1a))
* stream processor main ([59e5589](https://github.com/sb-icon/icon-governance/commit/59e5589bc3e3863a7f6b29bc555865fb428b5c41))

## [0.5.0](https://github.com/sb-icon/icon-governance/compare/v0.4.0...v0.5.0) (2023-09-16)


### Features

* add cron to get public key ([cec9bd0](https://github.com/sb-icon/icon-governance/commit/cec9bd0c971bb268f281361092468a8cc9c0085e))

## [0.4.0](https://github.com/sb-icon/icon-governance/compare/v0.3.1...v0.4.0) (2023-07-01)


### Features

* add rewards cron to preps [#18](https://github.com/sb-icon/icon-governance/issues/18) ([e61200a](https://github.com/sb-icon/icon-governance/commit/e61200a4dd8f602d49c35cb7cef4e0817b34063e))


### Bug Fixes

* add cron to update prep grade and add filter to remove unregistered preps [#16](https://github.com/sb-icon/icon-governance/issues/16) ([6499dce](https://github.com/sb-icon/icon-governance/commit/6499dcec69d027e02444f0cc6b6aab7fdcd2b862))

## [0.3.1](https://github.com/sb-icon/icon-governance/compare/v0.3.0...v0.3.1) (2023-04-26)


### Bug Fixes

* add contract delegations ([487fbe0](https://github.com/sb-icon/icon-governance/commit/487fbe0aaa0d7b8f82481155a97f749cfca3174d))

## [0.3.0](https://github.com/sb-icon/icon-governance/compare/v0.2.0...v0.3.0) (2023-03-21)


### Features

* add failures with endpoint params ([0bb88af](https://github.com/sb-icon/icon-governance/commit/0bb88af92c1414a11450f1a810b828d87b833149))

## [0.2.0](https://github.com/sb-icon/icon-governance/compare/v0.1.3...v0.2.0) (2023-03-08)


### Features

* add appscheduler and update all crons ([2896477](https://github.com/sb-icon/icon-governance/commit/2896477e8266548dea06e23e99355afefa095139))


### Bug Fixes

* add additional delegations cleaner [#6](https://github.com/sb-icon/icon-governance/issues/6) ([2f3db7d](https://github.com/sb-icon/icon-governance/commit/2f3db7d15cd23c725d8a83e30a366c224981a4f4))

## [0.1.3](https://github.com/sb-icon/icon-governance/compare/v0.1.2...v0.1.3) (2023-01-13)


### Bug Fixes

* remove zero delegations in cron icon-tracker[#69](https://github.com/sb-icon/icon-governance/issues/69) ([5b84020](https://github.com/sb-icon/icon-governance/commit/5b8402026a8585de26e0ae317d04c4098216e47b))
