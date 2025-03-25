import re
# Your input string
string = """
Assigned Facilities:
Node Node_1 is assigned to Facility Node_77
Node Node_2 is assigned to Facility Node_77
Node Node_3 is assigned to Facility Node_5
Node Node_4 is assigned to Facility Node_5
Node Node_5 is assigned to Facility Node_5
Node Node_6 is assigned to Facility Node_5
Node Node_7 is assigned to Facility Node_5
Node Node_8 is assigned to Facility Node_285
Node Node_9 is assigned to Facility Node_285
Node Node_10 is assigned to Facility Node_285
Node Node_11 is assigned to Facility Node_339
Node Node_12 is assigned to Facility Node_285
Node Node_13 is assigned to Facility Node_285
Node Node_14 is assigned to Facility Node_285
Node Node_15 is assigned to Facility Node_285
Node Node_16 is assigned to Facility Node_285
Node Node_17 is assigned to Facility Node_285
Node Node_18 is assigned to Facility Node_285
Node Node_19 is assigned to Facility Node_285
Node Node_20 is assigned to Facility Node_285
Node Node_21 is assigned to Facility Node_285
Node Node_22 is assigned to Facility Node_285
Node Node_23 is assigned to Facility Node_285
Node Node_24 is assigned to Facility Node_77
Node Node_25 is assigned to Facility Node_5
Node Node_26 is assigned to Facility Node_285
Node Node_27 is assigned to Facility Node_285
Node Node_28 is assigned to Facility Node_285
Node Node_29 is assigned to Facility Node_5
Node Node_30 is assigned to Facility Node_5
Node Node_31 is assigned to Facility Node_77
Node Node_32 is assigned to Facility Node_77
Node Node_33 is assigned to Facility Node_791
Node Node_34 is assigned to Facility Node_791
Node Node_35 is assigned to Facility Node_791
Node Node_36 is assigned to Facility Node_791
Node Node_37 is assigned to Facility Node_791
Node Node_38 is assigned to Facility Node_339
Node Node_39 is assigned to Facility Node_791
Node Node_40 is assigned to Facility Node_791
Node Node_41 is assigned to Facility Node_791
Node Node_42 is assigned to Facility Node_339
Node Node_43 is assigned to Facility Node_339
Node Node_44 is assigned to Facility Node_339
Node Node_45 is assigned to Facility Node_285
Node Node_46 is assigned to Facility Node_339
Node Node_47 is assigned to Facility Node_5
Node Node_48 is assigned to Facility Node_791
Node Node_49 is assigned to Facility Node_791
Node Node_50 is assigned to Facility Node_791
Node Node_51 is assigned to Facility Node_791
Node Node_52 is assigned to Facility Node_791
Node Node_53 is assigned to Facility Node_791
Node Node_54 is assigned to Facility Node_343
Node Node_55 is assigned to Facility Node_579
Node Node_56 is assigned to Facility Node_579
Node Node_57 is assigned to Facility Node_659
Node Node_58 is assigned to Facility Node_771
Node Node_59 is assigned to Facility Node_771
Node Node_60 is assigned to Facility Node_771
Node Node_61 is assigned to Facility Node_77
Node Node_62 is assigned to Facility Node_77
Node Node_63 is assigned to Facility Node_77
Node Node_64 is assigned to Facility Node_77
Node Node_65 is assigned to Facility Node_77
Node Node_66 is assigned to Facility Node_77
Node Node_67 is assigned to Facility Node_77
Node Node_68 is assigned to Facility Node_77
Node Node_69 is assigned to Facility Node_77
Node Node_70 is assigned to Facility Node_77
Node Node_71 is assigned to Facility Node_77
Node Node_72 is assigned to Facility Node_77
Node Node_73 is assigned to Facility Node_77
Node Node_74 is assigned to Facility Node_77
Node Node_75 is assigned to Facility Node_77
Node Node_76 is assigned to Facility Node_77
Node Node_77 is assigned to Facility Node_77
Node Node_78 is assigned to Facility Node_771
Node Node_79 is assigned to Facility Node_771
Node Node_80 is assigned to Facility Node_771
Node Node_81 is assigned to Facility Node_86
Node Node_82 is assigned to Facility Node_86
Node Node_83 is assigned to Facility Node_86
Node Node_84 is assigned to Facility Node_86
Node Node_85 is assigned to Facility Node_86
Node Node_86 is assigned to Facility Node_86
Node Node_87 is assigned to Facility Node_86
Node Node_88 is assigned to Facility Node_86
Node Node_89 is assigned to Facility Node_86
Node Node_90 is assigned to Facility Node_86
Node Node_91 is assigned to Facility Node_86
Node Node_92 is assigned to Facility Node_86
Node Node_93 is assigned to Facility Node_86
Node Node_94 is assigned to Facility Node_86
Node Node_95 is assigned to Facility Node_86
Node Node_96 is assigned to Facility Node_86
Node Node_97 is assigned to Facility Node_86
Node Node_98 is assigned to Facility Node_86
Node Node_99 is assigned to Facility Node_86
Node Node_100 is assigned to Facility Node_343
Node Node_101 is assigned to Facility Node_343
Node Node_102 is assigned to Facility Node_144
Node Node_103 is assigned to Facility Node_106
Node Node_104 is assigned to Facility Node_144
Node Node_105 is assigned to Facility Node_106
Node Node_106 is assigned to Facility Node_106
Node Node_107 is assigned to Facility Node_106
Node Node_108 is assigned to Facility Node_727
Node Node_109 is assigned to Facility Node_727
Node Node_110 is assigned to Facility Node_77
Node Node_111 is assigned to Facility Node_77
Node Node_112 is assigned to Facility Node_659
Node Node_113 is assigned to Facility Node_659
Node Node_114 is assigned to Facility Node_659
Node Node_115 is assigned to Facility Node_659
Node Node_116 is assigned to Facility Node_695
Node Node_117 is assigned to Facility Node_695
Node Node_118 is assigned to Facility Node_695
Node Node_119 is assigned to Facility Node_695
Node Node_120 is assigned to Facility Node_659
Node Node_121 is assigned to Facility Node_659
Node Node_122 is assigned to Facility Node_659
Node Node_123 is assigned to Facility Node_659
Node Node_124 is assigned to Facility Node_659
Node Node_125 is assigned to Facility Node_659
Node Node_126 is assigned to Facility Node_343
Node Node_127 is assigned to Facility Node_343
Node Node_128 is assigned to Facility Node_538
Node Node_129 is assigned to Facility Node_538
Node Node_130 is assigned to Facility Node_321
Node Node_131 is assigned to Facility Node_136
Node Node_132 is assigned to Facility Node_136
Node Node_133 is assigned to Facility Node_136
Node Node_134 is assigned to Facility Node_136
Node Node_135 is assigned to Facility Node_136
Node Node_136 is assigned to Facility Node_136
Node Node_137 is assigned to Facility Node_579
Node Node_138 is assigned to Facility Node_771
Node Node_139 is assigned to Facility Node_771
Node Node_140 is assigned to Facility Node_771
Node Node_141 is assigned to Facility Node_771
Node Node_142 is assigned to Facility Node_144
Node Node_143 is assigned to Facility Node_144
Node Node_144 is assigned to Facility Node_144
Node Node_145 is assigned to Facility Node_77
Node Node_146 is assigned to Facility Node_695
Node Node_147 is assigned to Facility Node_695
Node Node_148 is assigned to Facility Node_771
Node Node_149 is assigned to Facility Node_538
Node Node_150 is assigned to Facility Node_538
Node Node_151 is assigned to Facility Node_538
Node Node_152 is assigned to Facility Node_771
Node Node_153 is assigned to Facility Node_695
Node Node_154 is assigned to Facility Node_695
Node Node_155 is assigned to Facility Node_695
Node Node_156 is assigned to Facility Node_695
Node Node_157 is assigned to Facility Node_695
Node Node_158 is assigned to Facility Node_695
Node Node_159 is assigned to Facility Node_695
Node Node_160 is assigned to Facility Node_695
Node Node_161 is assigned to Facility Node_695
Node Node_162 is assigned to Facility Node_695
Node Node_163 is assigned to Facility Node_695
Node Node_164 is assigned to Facility Node_144
Node Node_166 is assigned to Facility Node_771
Node Node_167 is assigned to Facility Node_771
Node Node_168 is assigned to Facility Node_173
Node Node_169 is assigned to Facility Node_173
Node Node_170 is assigned to Facility Node_173
Node Node_171 is assigned to Facility Node_173
Node Node_172 is assigned to Facility Node_173
Node Node_173 is assigned to Facility Node_173
Node Node_174 is assigned to Facility Node_173
Node Node_175 is assigned to Facility Node_173
Node Node_176 is assigned to Facility Node_173
Node Node_177 is assigned to Facility Node_791
Node Node_178 is assigned to Facility Node_173
Node Node_179 is assigned to Facility Node_173
Node Node_180 is assigned to Facility Node_173
Node Node_181 is assigned to Facility Node_173
Node Node_182 is assigned to Facility Node_173
Node Node_183 is assigned to Facility Node_405
Node Node_184 is assigned to Facility Node_405
Node Node_185 is assigned to Facility Node_405
Node Node_186 is assigned to Facility Node_405
Node Node_187 is assigned to Facility Node_405
Node Node_188 is assigned to Facility Node_405
Node Node_189 is assigned to Facility Node_405
Node Node_190 is assigned to Facility Node_405
Node Node_191 is assigned to Facility Node_405
Node Node_192 is assigned to Facility Node_405
Node Node_193 is assigned to Facility Node_405
Node Node_194 is assigned to Facility Node_405
Node Node_195 is assigned to Facility Node_405
Node Node_196 is assigned to Facility Node_405
Node Node_197 is assigned to Facility Node_405
Node Node_198 is assigned to Facility Node_405
Node Node_199 is assigned to Facility Node_405
Node Node_200 is assigned to Facility Node_405
Node Node_201 is assigned to Facility Node_173
Node Node_202 is assigned to Facility Node_173
Node Node_203 is assigned to Facility Node_173
Node Node_204 is assigned to Facility Node_173
Node Node_205 is assigned to Facility Node_173
Node Node_206 is assigned to Facility Node_457
Node Node_207 is assigned to Facility Node_457
Node Node_208 is assigned to Facility Node_173
Node Node_209 is assigned to Facility Node_457
Node Node_210 is assigned to Facility Node_173
Node Node_211 is assigned to Facility Node_457
Node Node_212 is assigned to Facility Node_457
Node Node_213 is assigned to Facility Node_457
Node Node_214 is assigned to Facility Node_339
Node Node_215 is assigned to Facility Node_339
Node Node_216 is assigned to Facility Node_173
Node Node_217 is assigned to Facility Node_339
Node Node_218 is assigned to Facility Node_173
Node Node_219 is assigned to Facility Node_339
Node Node_220 is assigned to Facility Node_339
Node Node_221 is assigned to Facility Node_339
Node Node_222 is assigned to Facility Node_173
Node Node_223 is assigned to Facility Node_173
Node Node_224 is assigned to Facility Node_173
Node Node_225 is assigned to Facility Node_339
Node Node_226 is assigned to Facility Node_791
Node Node_227 is assigned to Facility Node_791
Node Node_228 is assigned to Facility Node_339
Node Node_229 is assigned to Facility Node_339
Node Node_230 is assigned to Facility Node_791
Node Node_231 is assigned to Facility Node_405
Node Node_232 is assigned to Facility Node_791
Node Node_233 is assigned to Facility Node_405
Node Node_234 is assigned to Facility Node_405
Node Node_235 is assigned to Facility Node_405
Node Node_236 is assigned to Facility Node_405
Node Node_237 is assigned to Facility Node_405
Node Node_238 is assigned to Facility Node_405
Node Node_239 is assigned to Facility Node_405
Node Node_240 is assigned to Facility Node_457
Node Node_241 is assigned to Facility Node_727
Node Node_242 is assigned to Facility Node_727
Node Node_243 is assigned to Facility Node_727
Node Node_244 is assigned to Facility Node_727
Node Node_245 is assigned to Facility Node_457
Node Node_246 is assigned to Facility Node_457
Node Node_247 is assigned to Facility Node_457
Node Node_248 is assigned to Facility Node_457
Node Node_249 is assigned to Facility Node_727
Node Node_250 is assigned to Facility Node_727
Node Node_251 is assigned to Facility Node_727
Node Node_252 is assigned to Facility Node_173
Node Node_253 is assigned to Facility Node_321
Node Node_254 is assigned to Facility Node_321
Node Node_255 is assigned to Facility Node_727
Node Node_256 is assigned to Facility Node_339
Node Node_257 is assigned to Facility Node_791
Node Node_258 is assigned to Facility Node_285
Node Node_259 is assigned to Facility Node_285
Node Node_260 is assigned to Facility Node_285
Node Node_261 is assigned to Facility Node_285
Node Node_262 is assigned to Facility Node_173
Node Node_263 is assigned to Facility Node_405
Node Node_264 is assigned to Facility Node_659
Node Node_265 is assigned to Facility Node_285
Node Node_266 is assigned to Facility Node_343
Node Node_267 is assigned to Facility Node_285
Node Node_268 is assigned to Facility Node_285
Node Node_269 is assigned to Facility Node_339
Node Node_270 is assigned to Facility Node_791
Node Node_271 is assigned to Facility Node_339
Node Node_272 is assigned to Facility Node_405
Node Node_273 is assigned to Facility Node_339
Node Node_274 is assigned to Facility Node_457
Node Node_275 is assigned to Facility Node_339
Node Node_276 is assigned to Facility Node_339
Node Node_277 is assigned to Facility Node_405
Node Node_278 is assigned to Facility Node_321
Node Node_279 is assigned to Facility Node_339
Node Node_280 is assigned to Facility Node_791
Node Node_281 is assigned to Facility Node_791
Node Node_282 is assigned to Facility Node_343
Node Node_283 is assigned to Facility Node_405
Node Node_284 is assigned to Facility Node_659
Node Node_285 is assigned to Facility Node_285
Node Node_286 is assigned to Facility Node_343
Node Node_287 is assigned to Facility Node_285
Node Node_288 is assigned to Facility Node_285
Node Node_289 is assigned to Facility Node_173
Node Node_290 is assigned to Facility Node_339
Node Node_291 is assigned to Facility Node_771
Node Node_292 is assigned to Facility Node_659
Node Node_293 is assigned to Facility Node_405
Node Node_294 is assigned to Facility Node_285
Node Node_296 is assigned to Facility Node_791
Node Node_297 is assigned to Facility Node_339
Node Node_298 is assigned to Facility Node_5
Node Node_299 is assigned to Facility Node_285
Node Node_300 is assigned to Facility Node_285
Node Node_301 is assigned to Facility Node_173
Node Node_302 is assigned to Facility Node_285
Node Node_303 is assigned to Facility Node_285
Node Node_304 is assigned to Facility Node_659
Node Node_305 is assigned to Facility Node_771
Node Node_306 is assigned to Facility Node_285
Node Node_307 is assigned to Facility Node_695
Node Node_308 is assigned to Facility Node_285
Node Node_309 is assigned to Facility Node_285
Node Node_310 is assigned to Facility Node_695
Node Node_311 is assigned to Facility Node_86
Node Node_312 is assigned to Facility Node_285
Node Node_313 is assigned to Facility Node_579
Node Node_314 is assigned to Facility Node_285
Node Node_315 is assigned to Facility Node_339
Node Node_316 is assigned to Facility Node_285
Node Node_317 is assigned to Facility Node_405
Node Node_318 is assigned to Facility Node_86
Node Node_319 is assigned to Facility Node_86
Node Node_320 is assigned to Facility Node_321
Node Node_321 is assigned to Facility Node_321
Node Node_322 is assigned to Facility Node_321
Node Node_323 is assigned to Facility Node_321
Node Node_324 is assigned to Facility Node_343
Node Node_325 is assigned to Facility Node_343
Node Node_326 is assigned to Facility Node_405
Node Node_327 is assigned to Facility Node_343
Node Node_328 is assigned to Facility Node_285
Node Node_329 is assigned to Facility Node_86
Node Node_330 is assigned to Facility Node_77
Node Node_331 is assigned to Facility Node_285
Node Node_332 is assigned to Facility Node_285
Node Node_333 is assigned to Facility Node_791
Node Node_334 is assigned to Facility Node_285
Node Node_335 is assigned to Facility Node_405
Node Node_336 is assigned to Facility Node_457
Node Node_337 is assigned to Facility Node_173
Node Node_338 is assigned to Facility Node_339
Node Node_339 is assigned to Facility Node_339
Node Node_340 is assigned to Facility Node_285
Node Node_341 is assigned to Facility Node_791
Node Node_342 is assigned to Facility Node_579
Node Node_343 is assigned to Facility Node_343
Node Node_344 is assigned to Facility Node_791
Node Node_345 is assigned to Facility Node_285
Node Node_346 is assigned to Facility Node_173
Node Node_347 is assigned to Facility Node_771
Node Node_348 is assigned to Facility Node_285
Node Node_349 is assigned to Facility Node_339
Node Node_350 is assigned to Facility Node_791
Node Node_351 is assigned to Facility Node_173
Node Node_352 is assigned to Facility Node_343
Node Node_353 is assigned to Facility Node_77
Node Node_354 is assigned to Facility Node_343
Node Node_355 is assigned to Facility Node_86
Node Node_356 is assigned to Facility Node_77
Node Node_357 is assigned to Facility Node_321
Node Node_358 is assigned to Facility Node_695
Node Node_359 is assigned to Facility Node_339
Node Node_360 is assigned to Facility Node_457
Node Node_361 is assigned to Facility Node_538
Node Node_362 is assigned to Facility Node_5
Node Node_363 is assigned to Facility Node_285
Node Node_364 is assigned to Facility Node_77
Node Node_365 is assigned to Facility Node_5
Node Node_366 is assigned to Facility Node_5
Node Node_367 is assigned to Facility Node_5
Node Node_368 is assigned to Facility Node_285
Node Node_369 is assigned to Facility Node_659
Node Node_370 is assigned to Facility Node_86
Node Node_371 is assigned to Facility Node_86
Node Node_372 is assigned to Facility Node_791
Node Node_373 is assigned to Facility Node_791
Node Node_374 is assigned to Facility Node_405
Node Node_375 is assigned to Facility Node_457
Node Node_376 is assigned to Facility Node_173
Node Node_377 is assigned to Facility Node_791
Node Node_378 is assigned to Facility Node_771
Node Node_379 is assigned to Facility Node_339
Node Node_380 is assigned to Facility Node_405
Node Node_381 is assigned to Facility Node_173
Node Node_382 is assigned to Facility Node_405
Node Node_383 is assigned to Facility Node_173
Node Node_384 is assigned to Facility Node_173
Node Node_385 is assigned to Facility Node_86
Node Node_386 is assigned to Facility Node_173
Node Node_387 is assigned to Facility Node_173
Node Node_388 is assigned to Facility Node_136
Node Node_389 is assigned to Facility Node_339
Node Node_390 is assigned to Facility Node_457
Node Node_391 is assigned to Facility Node_791
Node Node_392 is assigned to Facility Node_285
Node Node_393 is assigned to Facility Node_339
Node Node_394 is assigned to Facility Node_791
Node Node_395 is assigned to Facility Node_77
Node Node_396 is assigned to Facility Node_285
Node Node_397 is assigned to Facility Node_405
Node Node_398 is assigned to Facility Node_173
Node Node_399 is assigned to Facility Node_173
Node Node_400 is assigned to Facility Node_173
Node Node_401 is assigned to Facility Node_405
Node Node_402 is assigned to Facility Node_791
Node Node_403 is assigned to Facility Node_771
Node Node_404 is assigned to Facility Node_173
Node Node_405 is assigned to Facility Node_405
Node Node_406 is assigned to Facility Node_405
Node Node_407 is assigned to Facility Node_173
Node Node_408 is assigned to Facility Node_77
Node Node_409 is assigned to Facility Node_173
Node Node_410 is assigned to Facility Node_77
Node Node_411 is assigned to Facility Node_86
Node Node_412 is assigned to Facility Node_86
Node Node_413 is assigned to Facility Node_727
Node Node_414 is assigned to Facility Node_727
Node Node_415 is assigned to Facility Node_405
Node Node_416 is assigned to Facility Node_77
Node Node_417 is assigned to Facility Node_173
Node Node_418 is assigned to Facility Node_321
Node Node_419 is assigned to Facility Node_791
Node Node_420 is assigned to Facility Node_405
Node Node_421 is assigned to Facility Node_339
Node Node_422 is assigned to Facility Node_771
Node Node_423 is assigned to Facility Node_791
Node Node_424 is assigned to Facility Node_285
Node Node_425 is assigned to Facility Node_339
Node Node_426 is assigned to Facility Node_771
Node Node_427 is assigned to Facility Node_144
Node Node_428 is assigned to Facility Node_457
Node Node_430 is assigned to Facility Node_791
Node Node_431 is assigned to Facility Node_285
Node Node_432 is assigned to Facility Node_791
Node Node_433 is assigned to Facility Node_173
Node Node_434 is assigned to Facility Node_659
Node Node_435 is assigned to Facility Node_339
Node Node_436 is assigned to Facility Node_791
Node Node_437 is assigned to Facility Node_339
Node Node_438 is assigned to Facility Node_77
Node Node_439 is assigned to Facility Node_173
Node Node_440 is assigned to Facility Node_321
Node Node_441 is assigned to Facility Node_405
Node Node_442 is assigned to Facility Node_339
Node Node_443 is assigned to Facility Node_405
Node Node_444 is assigned to Facility Node_136
Node Node_445 is assigned to Facility Node_173
Node Node_446 is assigned to Facility Node_173
Node Node_447 is assigned to Facility Node_405
Node Node_448 is assigned to Facility Node_771
Node Node_449 is assigned to Facility Node_791
Node Node_450 is assigned to Facility Node_343
Node Node_451 is assigned to Facility Node_727
Node Node_452 is assigned to Facility Node_791
Node Node_453 is assigned to Facility Node_659
Node Node_454 is assigned to Facility Node_771
Node Node_455 is assigned to Facility Node_86
Node Node_456 is assigned to Facility Node_77
Node Node_457 is assigned to Facility Node_457
Node Node_458 is assigned to Facility Node_695
Node Node_459 is assigned to Facility Node_405
Node Node_460 is assigned to Facility Node_771
Node Node_461 is assigned to Facility Node_321
Node Node_462 is assigned to Facility Node_339
Node Node_463 is assigned to Facility Node_339
Node Node_464 is assigned to Facility Node_285
Node Node_465 is assigned to Facility Node_791
Node Node_466 is assigned to Facility Node_86
Node Node_467 is assigned to Facility Node_791
Node Node_468 is assigned to Facility Node_77
Node Node_469 is assigned to Facility Node_457
Node Node_470 is assigned to Facility Node_285
Node Node_471 is assigned to Facility Node_285
Node Node_472 is assigned to Facility Node_173
Node Node_473 is assigned to Facility Node_405
Node Node_474 is assigned to Facility Node_339
Node Node_475 is assigned to Facility Node_339
Node Node_476 is assigned to Facility Node_77
Node Node_477 is assigned to Facility Node_86
Node Node_478 is assigned to Facility Node_86
Node Node_479 is assigned to Facility Node_659
Node Node_480 is assigned to Facility Node_771
Node Node_481 is assigned to Facility Node_659
Node Node_482 is assigned to Facility Node_659
Node Node_483 is assigned to Facility Node_695
Node Node_484 is assigned to Facility Node_321
Node Node_485 is assigned to Facility Node_659
Node Node_486 is assigned to Facility Node_86
Node Node_487 is assigned to Facility Node_86
Node Node_488 is assigned to Facility Node_659
Node Node_489 is assigned to Facility Node_659
Node Node_490 is assigned to Facility Node_695
Node Node_491 is assigned to Facility Node_695
Node Node_492 is assigned to Facility Node_339
Node Node_493 is assigned to Facility Node_659
Node Node_494 is assigned to Facility Node_695
Node Node_495 is assigned to Facility Node_695
Node Node_496 is assigned to Facility Node_695
Node Node_497 is assigned to Facility Node_86
Node Node_498 is assigned to Facility Node_695
Node Node_499 is assigned to Facility Node_771
Node Node_500 is assigned to Facility Node_77
Node Node_501 is assigned to Facility Node_771
Node Node_502 is assigned to Facility Node_77
Node Node_503 is assigned to Facility Node_339
Node Node_504 is assigned to Facility Node_285
Node Node_505 is assigned to Facility Node_659
Node Node_506 is assigned to Facility Node_173
Node Node_507 is assigned to Facility Node_86
Node Node_508 is assigned to Facility Node_659
Node Node_509 is assigned to Facility Node_405
Node Node_510 is assigned to Facility Node_727
Node Node_511 is assigned to Facility Node_659
Node Node_512 is assigned to Facility Node_659
Node Node_513 is assigned to Facility Node_695
Node Node_514 is assigned to Facility Node_405
Node Node_515 is assigned to Facility Node_86
Node Node_516 is assigned to Facility Node_339
Node Node_517 is assigned to Facility Node_659
Node Node_518 is assigned to Facility Node_727
Node Node_519 is assigned to Facility Node_457
Node Node_520 is assigned to Facility Node_173
Node Node_521 is assigned to Facility Node_695
Node Node_522 is assigned to Facility Node_659
Node Node_523 is assigned to Facility Node_659
Node Node_524 is assigned to Facility Node_405
Node Node_525 is assigned to Facility Node_339
Node Node_526 is assigned to Facility Node_695
Node Node_527 is assigned to Facility Node_791
Node Node_528 is assigned to Facility Node_771
Node Node_529 is assigned to Facility Node_727
Node Node_530 is assigned to Facility Node_173
Node Node_531 is assigned to Facility Node_457
Node Node_532 is assigned to Facility Node_771
Node Node_533 is assigned to Facility Node_791
Node Node_534 is assigned to Facility Node_339
Node Node_535 is assigned to Facility Node_695
Node Node_536 is assigned to Facility Node_457
Node Node_537 is assigned to Facility Node_457
Node Node_538 is assigned to Facility Node_538
Node Node_539 is assigned to Facility Node_405
Node Node_540 is assigned to Facility Node_659
Node Node_541 is assigned to Facility Node_285
Node Node_542 is assigned to Facility Node_405
Node Node_543 is assigned to Facility Node_791
Node Node_544 is assigned to Facility Node_791
Node Node_545 is assigned to Facility Node_285
Node Node_546 is assigned to Facility Node_457
Node Node_547 is assigned to Facility Node_77
Node Node_548 is assigned to Facility Node_405
Node Node_549 is assigned to Facility Node_405
Node Node_550 is assigned to Facility Node_405
Node Node_551 is assigned to Facility Node_791
Node Node_552 is assigned to Facility Node_727
Node Node_553 is assigned to Facility Node_791
Node Node_554 is assigned to Facility Node_695
Node Node_555 is assigned to Facility Node_173
Node Node_556 is assigned to Facility Node_695
Node Node_557 is assigned to Facility Node_285
Node Node_558 is assigned to Facility Node_173
Node Node_559 is assigned to Facility Node_659
Node Node_560 is assigned to Facility Node_771
Node Node_561 is assigned to Facility Node_659
Node Node_562 is assigned to Facility Node_405
Node Node_563 is assigned to Facility Node_339
Node Node_564 is assigned to Facility Node_405
Node Node_565 is assigned to Facility Node_77
Node Node_566 is assigned to Facility Node_339
Node Node_567 is assigned to Facility Node_285
Node Node_568 is assigned to Facility Node_771
Node Node_569 is assigned to Facility Node_791
Node Node_570 is assigned to Facility Node_791
Node Node_571 is assigned to Facility Node_173
Node Node_572 is assigned to Facility Node_405
Node Node_573 is assigned to Facility Node_339
Node Node_574 is assigned to Facility Node_405
Node Node_575 is assigned to Facility Node_173
Node Node_576 is assigned to Facility Node_77
Node Node_577 is assigned to Facility Node_285
Node Node_578 is assigned to Facility Node_321
Node Node_579 is assigned to Facility Node_579
Node Node_580 is assigned to Facility Node_339
Node Node_581 is assigned to Facility Node_695
Node Node_582 is assigned to Facility Node_771
Node Node_583 is assigned to Facility Node_343
Node Node_584 is assigned to Facility Node_791
Node Node_585 is assigned to Facility Node_771
Node Node_586 is assigned to Facility Node_321
Node Node_587 is assigned to Facility Node_659
Node Node_588 is assigned to Facility Node_791
Node Node_589 is assigned to Facility Node_173
Node Node_590 is assigned to Facility Node_339
Node Node_591 is assigned to Facility Node_77
Node Node_592 is assigned to Facility Node_791
Node Node_593 is assigned to Facility Node_77
Node Node_594 is assigned to Facility Node_173
Node Node_595 is assigned to Facility Node_173
Node Node_596 is assigned to Facility Node_86
Node Node_597 is assigned to Facility Node_659
Node Node_598 is assigned to Facility Node_771
Node Node_599 is assigned to Facility Node_695
Node Node_600 is assigned to Facility Node_136
Node Node_601 is assigned to Facility Node_285
Node Node_602 is assigned to Facility Node_659
Node Node_603 is assigned to Facility Node_405
Node Node_604 is assigned to Facility Node_339
Node Node_605 is assigned to Facility Node_659
Node Node_606 is assigned to Facility Node_173
Node Node_607 is assigned to Facility Node_405
Node Node_608 is assigned to Facility Node_727
Node Node_609 is assigned to Facility Node_339
Node Node_610 is assigned to Facility Node_285
Node Node_613 is assigned to Facility Node_285
Node Node_614 is assigned to Facility Node_77
Node Node_615 is assigned to Facility Node_5
Node Node_616 is assigned to Facility Node_343
Node Node_617 is assigned to Facility Node_77
Node Node_618 is assigned to Facility Node_173
Node Node_619 is assigned to Facility Node_339
Node Node_620 is assigned to Facility Node_791
Node Node_621 is assigned to Facility Node_791
Node Node_622 is assigned to Facility Node_457
Node Node_623 is assigned to Facility Node_86
Node Node_624 is assigned to Facility Node_173
Node Node_625 is assigned to Facility Node_86
Node Node_626 is assigned to Facility Node_771
Node Node_627 is assigned to Facility Node_285
Node Node_628 is assigned to Facility Node_77
Node Node_629 is assigned to Facility Node_791
Node Node_630 is assigned to Facility Node_339
Node Node_631 is assigned to Facility Node_77
Node Node_632 is assigned to Facility Node_285
Node Node_633 is assigned to Facility Node_339
Node Node_634 is assigned to Facility Node_771
Node Node_635 is assigned to Facility Node_695
Node Node_636 is assigned to Facility Node_405
Node Node_637 is assigned to Facility Node_405
Node Node_638 is assigned to Facility Node_77
Node Node_639 is assigned to Facility Node_77
Node Node_640 is assigned to Facility Node_173
Node Node_641 is assigned to Facility Node_339
Node Node_642 is assigned to Facility Node_285
Node Node_643 is assigned to Facility Node_695
Node Node_644 is assigned to Facility Node_144
Node Node_645 is assigned to Facility Node_285
Node Node_646 is assigned to Facility Node_321
Node Node_647 is assigned to Facility Node_727
Node Node_648 is assigned to Facility Node_285
Node Node_649 is assigned to Facility Node_791
Node Node_650 is assigned to Facility Node_321
Node Node_651 is assigned to Facility Node_771
Node Node_652 is assigned to Facility Node_321
Node Node_653 is assigned to Facility Node_321
Node Node_654 is assigned to Facility Node_173
Node Node_655 is assigned to Facility Node_173
Node Node_656 is assigned to Facility Node_405
Node Node_657 is assigned to Facility Node_339
Node Node_658 is assigned to Facility Node_405
Node Node_659 is assigned to Facility Node_659
Node Node_660 is assigned to Facility Node_321
Node Node_661 is assigned to Facility Node_727
Node Node_662 is assigned to Facility Node_659
Node Node_663 is assigned to Facility Node_457
Node Node_664 is assigned to Facility Node_457
Node Node_665 is assigned to Facility Node_771
Node Node_666 is assigned to Facility Node_339
Node Node_667 is assigned to Facility Node_136
Node Node_669 is assigned to Facility Node_339
Node Node_670 is assigned to Facility Node_457
Node Node_671 is assigned to Facility Node_727
Node Node_672 is assigned to Facility Node_771
Node Node_673 is assigned to Facility Node_339
Node Node_674 is assigned to Facility Node_339
Node Node_675 is assigned to Facility Node_173
Node Node_676 is assigned to Facility Node_791
Node Node_677 is assigned to Facility Node_405
Node Node_678 is assigned to Facility Node_106
Node Node_679 is assigned to Facility Node_727
Node Node_680 is assigned to Facility Node_771
Node Node_681 is assigned to Facility Node_339
Node Node_682 is assigned to Facility Node_173
Node Node_683 is assigned to Facility Node_405
Node Node_684 is assigned to Facility Node_321
Node Node_685 is assigned to Facility Node_339
Node Node_686 is assigned to Facility Node_173
Node Node_687 is assigned to Facility Node_343
Node Node_688 is assigned to Facility Node_695
Node Node_689 is assigned to Facility Node_77
Node Node_690 is assigned to Facility Node_285
Node Node_691 is assigned to Facility Node_771
Node Node_692 is assigned to Facility Node_77
Node Node_693 is assigned to Facility Node_77
Node Node_694 is assigned to Facility Node_771
Node Node_695 is assigned to Facility Node_695
Node Node_696 is assigned to Facility Node_695
Node Node_697 is assigned to Facility Node_695
Node Node_698 is assigned to Facility Node_771
Node Node_699 is assigned to Facility Node_771
Node Node_700 is assigned to Facility Node_659
Node Node_701 is assigned to Facility Node_86
Node Node_702 is assigned to Facility Node_405
Node Node_703 is assigned to Facility Node_285
Node Node_704 is assigned to Facility Node_405
Node Node_705 is assigned to Facility Node_457
Node Node_706 is assigned to Facility Node_86
Node Node_707 is assigned to Facility Node_791
Node Node_708 is assigned to Facility Node_173
Node Node_709 is assigned to Facility Node_659
Node Node_710 is assigned to Facility Node_695
Node Node_711 is assigned to Facility Node_339
Node Node_712 is assigned to Facility Node_727
Node Node_713 is assigned to Facility Node_771
Node Node_714 is assigned to Facility Node_771
Node Node_715 is assigned to Facility Node_538
Node Node_716 is assigned to Facility Node_695
Node Node_717 is assigned to Facility Node_457
Node Node_718 is assigned to Facility Node_405
Node Node_719 is assigned to Facility Node_285
Node Node_720 is assigned to Facility Node_173
Node Node_721 is assigned to Facility Node_405
Node Node_722 is assigned to Facility Node_285
Node Node_723 is assigned to Facility Node_457
Node Node_724 is assigned to Facility Node_77
Node Node_725 is assigned to Facility Node_405
Node Node_726 is assigned to Facility Node_405
Node Node_727 is assigned to Facility Node_727
Node Node_729 is assigned to Facility Node_339
Node Node_730 is assigned to Facility Node_659
Node Node_731 is assigned to Facility Node_173
Node Node_732 is assigned to Facility Node_86
Node Node_733 is assigned to Facility Node_457
Node Node_734 is assigned to Facility Node_659
Node Node_735 is assigned to Facility Node_339
Node Node_736 is assigned to Facility Node_285
Node Node_737 is assigned to Facility Node_285
Node Node_738 is assigned to Facility Node_285
Node Node_739 is assigned to Facility Node_285
Node Node_740 is assigned to Facility Node_285
Node Node_741 is assigned to Facility Node_285
Node Node_742 is assigned to Facility Node_339
Node Node_743 is assigned to Facility Node_285
Node Node_744 is assigned to Facility Node_343
Node Node_745 is assigned to Facility Node_285
Node Node_746 is assigned to Facility Node_321
Node Node_747 is assigned to Facility Node_285
Node Node_748 is assigned to Facility Node_285
Node Node_749 is assigned to Facility Node_173
Node Node_750 is assigned to Facility Node_457
Node Node_751 is assigned to Facility Node_173
Node Node_752 is assigned to Facility Node_77
Node Node_753 is assigned to Facility Node_144
Node Node_754 is assigned to Facility Node_791
Node Node_755 is assigned to Facility Node_77
Node Node_756 is assigned to Facility Node_579
Node Node_757 is assigned to Facility Node_106
Node Node_758 is assigned to Facility Node_791
Node Node_759 is assigned to Facility Node_77
Node Node_760 is assigned to Facility Node_77
Node Node_761 is assigned to Facility Node_136
Node Node_762 is assigned to Facility Node_791
Node Node_763 is assigned to Facility Node_285
Node Node_764 is assigned to Facility Node_457
Node Node_765 is assigned to Facility Node_173
Node Node_766 is assigned to Facility Node_457
Node Node_767 is assigned to Facility Node_321
Node Node_768 is assigned to Facility Node_405
Node Node_769 is assigned to Facility Node_457
Node Node_770 is assigned to Facility Node_405
Node Node_771 is assigned to Facility Node_771
Node Node_772 is assigned to Facility Node_659
Node Node_773 is assigned to Facility Node_405
Node Node_774 is assigned to Facility Node_405
Node Node_775 is assigned to Facility Node_173
Node Node_776 is assigned to Facility Node_173
Node Node_777 is assigned to Facility Node_791
Node Node_778 is assigned to Facility Node_405
Node Node_779 is assigned to Facility Node_173
Node Node_780 is assigned to Facility Node_405
Node Node_781 is assigned to Facility Node_405
Node Node_782 is assigned to Facility Node_77
Node Node_783 is assigned to Facility Node_173
Node Node_784 is assigned to Facility Node_173
Node Node_785 is assigned to Facility Node_339
Node Node_786 is assigned to Facility Node_405
Node Node_787 is assigned to Facility Node_339
Node Node_788 is assigned to Facility Node_405
Node Node_789 is assigned to Facility Node_173
Node Node_790 is assigned to Facility Node_339
Node Node_791 is assigned to Facility Node_791
Node Node_792 is assigned to Facility Node_771
Node Node_793 is assigned to Facility Node_771
Node Node_794 is assigned to Facility Node_659
Node Node_795 is assigned to Facility Node_457
Node Node_796 is assigned to Facility Node_538
Node Node_797 is assigned to Facility Node_86
Node Node_798 is assigned to Facility Node_771
Node Node_799 is assigned to Facility Node_5
Node Node_800 is assigned to Facility Node_5
Node Node_801 is assigned to Facility Node_727
Node Node_802 is assigned to Facility Node_791
Node Node_803 is assigned to Facility Node_659
Node Node_804 is assigned to Facility Node_771
Node Node_805 is assigned to Facility Node_771
Node Node_806 is assigned to Facility Node_659
Node Node_807 is assigned to Facility Node_86
Node Node_808 is assigned to Facility Node_339
Node Node_809 is assigned to Facility Node_727
Node Node_810 is assigned to Facility Node_791
Node Node_811 is assigned to Facility Node_405
Node Node_812 is assigned to Facility Node_339
Node Node_813 is assigned to Facility Node_173
Node Node_814 is assigned to Facility Node_457
Node Node_815 is assigned to Facility Node_173
Node Node_816 is assigned to Facility Node_339
Node Node_817 is assigned to Facility Node_405
Node Node_818 is assigned to Facility Node_659
Node Node_819 is assigned to Facility Node_771
Node Node_820 is assigned to Facility Node_173
Node Node_821 is assigned to Facility Node_339
Node Node_822 is assigned to Facility Node_173
Node Node_823 is assigned to Facility Node_173
Node Node_824 is assigned to Facility Node_86
Node Node_825 is assigned to Facility Node_173

Open Facilities:
['Node_5', 'Node_77', 'Node_86', 'Node_106', 'Node_136', 'Node_144', 'Node_173', 'Node_285', 'Node_321', 'Node_339', 'Node_343', 'Node_405', 'Node_457', 'Node_538', 'Node_579', 'Node_659', 'Node_695', 'Node_727', 'Node_771', 'Node_791']
"""



def parse_assignments(text):
    assignments = {}
    for line in text.split('\n'):
        match = re.search(r'Node Node_(\d+) is assigned to Facility Node_(\d+)', line)
        if match:
            node = int(match.group(1))
            facility = int(match.group(2))
            if facility not in assignments:
                assignments[facility] = set()
            assignments[facility].add(node)
    return assignments

def generate_sql_query():
    assignments = parse_assignments(string)
    open_facilities = [int(f.split('_')[1]) for f in eval(string.split('Open Facilities:\n')[-1].strip())]
    
    query_parts = []
    for facility in open_facilities:
        if facility in assignments:
            nodes = assignments[facility]
            query_parts.append(f"(OriginID = {facility} AND DestinationID IN ({','.join(map(str, nodes))}))")
    
    return ' OR '.join(query_parts)

def extract_facility_ids():
    facilities_str = string.split('Open Facilities:\n')[-1].strip()
    facilities_list = eval(facilities_str)
    # Extract just the numbers from each Node_XXX string
    facility_ids = [int(f.split('_')[1]) for f in facilities_list]
    return ', '.join(map(str, facility_ids))

# Print the SQL query
print(generate_sql_query())

# Print the facility IDs in the requested format
print("\nFacility IDs:")
print(extract_facility_ids())

