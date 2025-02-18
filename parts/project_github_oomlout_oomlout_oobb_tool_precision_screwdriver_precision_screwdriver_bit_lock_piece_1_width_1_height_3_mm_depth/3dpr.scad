$fn = 50;


difference() {
	union() {
		translate(v = [-4.0000000000, -3.0000000000, 0]) {
			cube(size = [8, 6, 7]);
		}
	}
	union() {
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						#linear_extrude(height = 2.5000000000) {
							polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
						}
					}
					union();
				}
			}
		}
		translate(v = [0, 0, 7]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						#translate(v = [0, 0, -25.0000000000]) {
							cylinder(h = 25, r = 1.5000000000);
						}
						#cylinder(h = 253.2000000000, r = 3.0000000000);
						#translate(v = [0, 0, -25.0000000000]) {
							cylinder(h = 25, r = 1.8000000000);
						}
						#translate(v = [0, 0, -25.0000000000]) {
							cylinder(h = 25, r = 1.5000000000);
						}
					}
					union();
				}
			}
		}
	}
}