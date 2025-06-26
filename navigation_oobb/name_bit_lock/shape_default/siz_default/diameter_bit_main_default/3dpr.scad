$fn = 50;


difference() {
	union() {
		translate(v = [-3.5000000000, -1.5000000000, 0]) {
			cube(size = [7, 3, 14]);
		}
	}
	union() {
		translate(v = [0, -1.5000000000, 9.0000000000]) {
			rotate(a = [0, 90, 90]) {
				difference() {
					union() {
						#hull() {
							#translate(v = [2.5000000000, 0, 0]) {
								cylinder(h = 3, r = 1.8000000000, r1 = 1.8000000000, r2 = 1.8000000000);
							}
							#translate(v = [-2.5000000000, 0, 0]) {
								cylinder(h = 3, r = 1.8000000000, r1 = 1.8000000000, r2 = 1.8000000000);
							}
						}
					}
					union();
				}
			}
		}
	}
}