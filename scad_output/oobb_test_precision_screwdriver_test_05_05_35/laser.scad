$fn = 50;


difference() {
	union() {
		translate(v = [0, 50, 0]) {
			rotate(a = [180, 0, 0]) {
				difference() {
					union() {
						rotate(a = [0, 90, 0]) {
							linear_extrude(height = 60) {
								polygon(points = [[6.0000000000, 0.0000000000], [3.0000000000, 5.1961524227], [-3.0000000000, 5.1961524227], [-6.0000000000, 0.0000000000], [-3.0000000000, -5.1961524227], [3.0000000000, -5.1961524227]]);
							}
						}
						translate(v = [10, 0, 0.0000000000]) {
							rotate(a = [0, 90, 0]) {
								cylinder(h = 50, r = 8);
							}
						}
					}
					union() {
						translate(v = [35, 0, 6.0000000000]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										translate(v = [0, 0, -9.5000000000]) {
											rotate(a = [0, 0, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, -150]) {
															#linear_extrude(height = 150) {
																polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
															}
														}
													}
													union();
												}
											}
										}
										translate(v = [0, 0, -9.0000000000]) {
											rotate(a = [0, 0, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, -150]) {
															#linear_extrude(height = 150) {
																polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
															}
														}
													}
													union();
												}
											}
										}
										translate(v = [0, 0, -9.5000000000]) {
											rotate(a = [0, 0, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, -150]) {
															#linear_extrude(height = 150) {
																polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
															}
														}
													}
													union();
												}
											}
										}
										#translate(v = [0, 0, -1.7000000000]) {
											cylinder(h = 1.7000000000, r1 = 1.5000000000, r2 = 2.4000000000);
										}
										#cylinder(h = 50, r = 2.4000000000);
										#translate(v = [0, 0, -12.0000000000]) {
											cylinder(h = 12, r = 1.5000000000);
										}
										#translate(v = [0, 0, -12.0000000000]) {
											cylinder(h = 12, r = 1.8000000000);
										}
										#translate(v = [0, 0, -12.0000000000]) {
											cylinder(h = 12, r = 1.5000000000);
										}
									}
									union();
								}
							}
						}
						translate(v = [50, 0, -6.0000000000]) {
							rotate(a = [0, 180, 0]) {
								difference() {
									union() {
										translate(v = [0, 0, -9.5000000000]) {
											rotate(a = [0, 0, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, -150]) {
															#linear_extrude(height = 150) {
																polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
															}
														}
													}
													union();
												}
											}
										}
										translate(v = [0, 0, -9.0000000000]) {
											rotate(a = [0, 0, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, -150]) {
															#linear_extrude(height = 150) {
																polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
															}
														}
													}
													union();
												}
											}
										}
										translate(v = [0, 0, -9.5000000000]) {
											rotate(a = [0, 0, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, -150]) {
															#linear_extrude(height = 150) {
																polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
															}
														}
													}
													union();
												}
											}
										}
										#translate(v = [0, 0, -1.7000000000]) {
											cylinder(h = 1.7000000000, r1 = 1.5000000000, r2 = 2.4000000000);
										}
										#cylinder(h = 50, r = 2.4000000000);
										#translate(v = [0, 0, -12.0000000000]) {
											cylinder(h = 12, r = 1.5000000000);
										}
										#translate(v = [0, 0, -12.0000000000]) {
											cylinder(h = 12, r = 1.8000000000);
										}
										#translate(v = [0, 0, -12.0000000000]) {
											cylinder(h = 12, r = 1.5000000000);
										}
									}
									union();
								}
							}
						}
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 90, 0]) {
								difference() {
									union() {
										translate(v = [0.2500000000, 0, 0]) {
											#linear_extrude(height = 28.5000000000) {
												polygon(points = [[4.1658550000, 0.0000000000], [2.0829275000, 3.6077362585], [-2.0829275000, 3.6077362585], [-4.1658550000, 0.0000000000], [-2.0829275000, -3.6077362585], [2.0829275000, -3.6077362585]]);
											}
										}
										#translate(v = [0, 0, -72.0000000000]) {
											cylinder(h = 100, r = 2.7500000000);
										}
									}
									union() {
										translate(v = [0, 0, 17]) {
											#rotate_extrude(angle = 360) {
												translate(v = [5.8500000000, 0, 0]) {
													circle(r = 3.7187500000);
												}
											}
										}
										difference() {
											#cylinder(h = 2, r1 = 10.7500000000, r2 = 11.9250000000);
											#cylinder(h = 2, r1 = 2.7500000000, r2 = 3.9250000000);
										}
									}
								}
							}
						}
					}
				}
			}
		}
		rotate(a = [0, 90, 0]) {
			linear_extrude(height = 60) {
				polygon(points = [[6.0000000000, 0.0000000000], [3.0000000000, 5.1961524227], [-3.0000000000, 5.1961524227], [-6.0000000000, 0.0000000000], [-3.0000000000, -5.1961524227], [3.0000000000, -5.1961524227]]);
			}
		}
		translate(v = [10, 0, 0.0000000000]) {
			rotate(a = [0, 90, 0]) {
				cylinder(h = 50, r = 8);
			}
		}
	}
	union() {
		translate(v = [35, 0, 6.0000000000]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -9.5000000000]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										translate(v = [0, 0, -150]) {
											#linear_extrude(height = 150) {
												polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
											}
										}
									}
									union();
								}
							}
						}
						translate(v = [0, 0, -9.0000000000]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										translate(v = [0, 0, -150]) {
											#linear_extrude(height = 150) {
												polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
											}
										}
									}
									union();
								}
							}
						}
						translate(v = [0, 0, -9.5000000000]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										translate(v = [0, 0, -150]) {
											#linear_extrude(height = 150) {
												polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
											}
										}
									}
									union();
								}
							}
						}
						#translate(v = [0, 0, -1.7000000000]) {
							cylinder(h = 1.7000000000, r1 = 1.5000000000, r2 = 2.4000000000);
						}
						#cylinder(h = 50, r = 2.4000000000);
						#translate(v = [0, 0, -12.0000000000]) {
							cylinder(h = 12, r = 1.5000000000);
						}
						#translate(v = [0, 0, -12.0000000000]) {
							cylinder(h = 12, r = 1.8000000000);
						}
						#translate(v = [0, 0, -12.0000000000]) {
							cylinder(h = 12, r = 1.5000000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [50, 0, -6.0000000000]) {
			rotate(a = [0, 180, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -9.5000000000]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										translate(v = [0, 0, -150]) {
											#linear_extrude(height = 150) {
												polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
											}
										}
									}
									union();
								}
							}
						}
						translate(v = [0, 0, -9.0000000000]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										translate(v = [0, 0, -150]) {
											#linear_extrude(height = 150) {
												polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
											}
										}
									}
									union();
								}
							}
						}
						translate(v = [0, 0, -9.5000000000]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										translate(v = [0, 0, -150]) {
											#linear_extrude(height = 150) {
												polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
											}
										}
									}
									union();
								}
							}
						}
						#translate(v = [0, 0, -1.7000000000]) {
							cylinder(h = 1.7000000000, r1 = 1.5000000000, r2 = 2.4000000000);
						}
						#cylinder(h = 50, r = 2.4000000000);
						#translate(v = [0, 0, -12.0000000000]) {
							cylinder(h = 12, r = 1.5000000000);
						}
						#translate(v = [0, 0, -12.0000000000]) {
							cylinder(h = 12, r = 1.8000000000);
						}
						#translate(v = [0, 0, -12.0000000000]) {
							cylinder(h = 12, r = 1.5000000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 90, 0]) {
				difference() {
					union() {
						translate(v = [0.2500000000, 0, 0]) {
							#linear_extrude(height = 28.5000000000) {
								polygon(points = [[4.1658550000, 0.0000000000], [2.0829275000, 3.6077362585], [-2.0829275000, 3.6077362585], [-4.1658550000, 0.0000000000], [-2.0829275000, -3.6077362585], [2.0829275000, -3.6077362585]]);
							}
						}
						#translate(v = [0, 0, -72.0000000000]) {
							cylinder(h = 100, r = 2.7500000000);
						}
					}
					union() {
						translate(v = [0, 0, 17]) {
							#rotate_extrude(angle = 360) {
								translate(v = [5.8500000000, 0, 0]) {
									circle(r = 3.7187500000);
								}
							}
						}
						difference() {
							#cylinder(h = 2, r1 = 10.7500000000, r2 = 11.9250000000);
							#cylinder(h = 2, r1 = 2.7500000000, r2 = 3.9250000000);
						}
					}
				}
			}
		}
		translate(v = [-250.0000000000, -250.0000000000, 0]) {
			cube(size = [500, 500, 500]);
		}
		translate(v = [-250.0000000000, -250.0000000000, 0]) {
			cube(size = [500, 500, 500]);
		}
		translate(v = [-250.0000000000, -250.0000000000, 0]) {
			cube(size = [500, 500, 500]);
		}
	}
}