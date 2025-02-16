$fn = 50;


difference() {
	union() {
		cylinder(h = 3, r1 = 2.1250000000, r2 = 4.7735000000);
		translate(v = [0, 0, 9.0000000000]) {
			cylinder(h = 51, r = 5.0000000000);
		}
		translate(v = [0, 0, 55.0000000000]) {
			cylinder(h = 35, r1 = 5.0000000000, r2 = 9.0000000000);
		}
		translate(v = [0, 0, 90.0000000000]) {
			cylinder(h = 5, r = 9.0000000000);
		}
		translate(v = [0, 0, 3]) {
			linear_extrude(height = 6) {
				polygon(points = [[5.7735000000, 0.0000000000], [2.8867500000, 4.9999976687], [-2.8867500000, 4.9999976687], [-5.7735000000, 0.0000000000], [-2.8867500000, -4.9999976687], [2.8867500000, -4.9999976687]]);
			}
		}
		translate(v = [0, 0, 50]) {
			linear_extrude(height = 9) {
				polygon(points = [[7.5055500000, 0.0000000000], [3.7527750000, 6.4999969694], [-3.7527750000, 6.4999969694], [-7.5055500000, 0.0000000000], [-3.7527750000, -6.4999969694], [3.7527750000, -6.4999969694]]);
			}
		}
	}
	union() {
		rotate(a = [0, 0, 0.0000000000]) {
			translate(v = [0, 0, 0]) {
				translate(v = [81.0000000000, 0, 29.5000000000]) {
					rotate(a = [90, 0, 0]) {
						#rotate_extrude(angle = 360) {
							translate(v = [76.2500000000, 0, 0]) {
								circle(r = 1.2500000000);
							}
						}
					}
				}
			}
		}
		rotate(a = [0, 0, 60.0000000000]) {
			translate(v = [0, 0, 0]) {
				translate(v = [81.0000000000, 0, 29.5000000000]) {
					rotate(a = [90, 0, 0]) {
						#rotate_extrude(angle = 360) {
							translate(v = [76.2500000000, 0, 0]) {
								circle(r = 1.2500000000);
							}
						}
					}
				}
			}
		}
		rotate(a = [0, 0, 120.0000000000]) {
			translate(v = [0, 0, 0]) {
				translate(v = [81.0000000000, 0, 29.5000000000]) {
					rotate(a = [90, 0, 0]) {
						#rotate_extrude(angle = 360) {
							translate(v = [76.2500000000, 0, 0]) {
								circle(r = 1.2500000000);
							}
						}
					}
				}
			}
		}
		rotate(a = [0, 0, 180.0000000000]) {
			translate(v = [0, 0, 0]) {
				translate(v = [81.0000000000, 0, 29.5000000000]) {
					rotate(a = [90, 0, 0]) {
						#rotate_extrude(angle = 360) {
							translate(v = [76.2500000000, 0, 0]) {
								circle(r = 1.2500000000);
							}
						}
					}
				}
			}
		}
		rotate(a = [0, 0, 240.0000000000]) {
			translate(v = [0, 0, 0]) {
				translate(v = [81.0000000000, 0, 29.5000000000]) {
					rotate(a = [90, 0, 0]) {
						#rotate_extrude(angle = 360) {
							translate(v = [76.2500000000, 0, 0]) {
								circle(r = 1.2500000000);
							}
						}
					}
				}
			}
		}
		rotate(a = [0, 0, 300.0000000000]) {
			translate(v = [0, 0, 0]) {
				translate(v = [81.0000000000, 0, 29.5000000000]) {
					rotate(a = [90, 0, 0]) {
						#rotate_extrude(angle = 360) {
							translate(v = [76.2500000000, 0, 0]) {
								circle(r = 1.2500000000);
							}
						}
					}
				}
			}
		}
		translate(v = [0, 0, 33.1000000000]) {
			rotate_extrude(angle = 360) {
				translate(v = [79.0000000000, 0, 0]) {
					circle(r = 75.0000000000);
				}
			}
		}
		translate(v = [0, 0, 31.3000000000]) {
			rotate_extrude(angle = 360) {
				translate(v = [79.0000000000, 0, 0]) {
					circle(r = 75.0000000000);
				}
			}
		}
		translate(v = [0, 0, 27.7000000000]) {
			rotate_extrude(angle = 360) {
				translate(v = [79.0000000000, 0, 0]) {
					circle(r = 75.0000000000);
				}
			}
		}
		translate(v = [0, 0, 25.9000000000]) {
			rotate_extrude(angle = 360) {
				translate(v = [79.0000000000, 0, 0]) {
					circle(r = 75.0000000000);
				}
			}
		}
		translate(v = [0, 0, 69.2500000000]) {
			rotate_extrude(angle = 360) {
				translate(v = [80.5000000000, 0, 0]) {
					circle(r = 75.0000000000);
				}
			}
		}
		translate(v = [0, 0, 79.5000000000]) {
			rotate_extrude(angle = 360) {
				translate(v = [15.0000000000, 0, 0]) {
					circle(r = 8.0000000000);
				}
			}
		}
	}
}