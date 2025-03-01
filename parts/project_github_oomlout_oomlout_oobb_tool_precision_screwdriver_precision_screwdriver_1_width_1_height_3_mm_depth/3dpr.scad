$fn = 50;


difference() {
	union() {
		cylinder(h = 3, r1 = 1.2500000000, r2 = 6.0000000000);
		translate(v = [0, 0, 3]) {
			linear_extrude(height = 9) {
				polygon(points = [[5.7735000000, 0.0000000000], [2.8867500000, 4.9999976687], [-2.8867500000, 4.9999976687], [-5.7735000000, 0.0000000000], [-2.8867500000, -4.9999976687], [2.8867500000, -4.9999976687]]);
			}
		}
		translate(v = [0, 0, 12.0000000000]) {
			cylinder(h = 40, r = 6.0000000000);
		}
		translate(v = [0, 0, 52]) {
			linear_extrude(height = 9) {
				polygon(points = [[7.5055500000, 0.0000000000], [3.7527750000, 6.4999969694], [-3.7527750000, 6.4999969694], [-7.5055500000, 0.0000000000], [-3.7527750000, -6.4999969694], [3.7527750000, -6.4999969694]]);
			}
		}
		translate(v = [0, 0, 61.0000000000]) {
			cylinder(h = 35, r = 6.0000000000);
		}
		translate(v = [0, 0, 96.0000000000]) {
			cylinder(h = 6, r = 8.2500000000);
		}
		translate(v = [0, 0, 96.0000000000]) {
			cylinder(h = 5.2500000000, r = 9.0000000000);
		}
		translate(v = [0, 0, 101.2500000000]) {
			rotate_extrude(angle = 360) {
				translate(v = [8.2500000000, 0, 0]) {
					circle(r = 0.7500000000);
				}
			}
		}
	}
	union() {
		translate(v = [0, 0, 25]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0.1000000000, 0, 0]) {
							#linear_extrude(height = 228.2000000000) {
								polygon(points = [[3.8658550000, 0.0000000000], [1.9329275000, 3.3479286373], [-1.9329275000, 3.3479286373], [-3.8658550000, 0.0000000000], [-1.9329275000, -3.3479286373], [1.9329275000, -3.3479286373]]);
							}
						}
						#translate(v = [0, 0, -71.8000000000]) {
							cylinder(h = 100, r = 1.8500000000);
						}
					}
					union() {
						difference() {
							#cylinder(h = 2, r1 = 9.8500000000, r2 = 11.7750000000);
							#cylinder(h = 2, r1 = 1.8500000000, r2 = 3.7750000000);
						}
					}
				}
			}
		}
	}
}