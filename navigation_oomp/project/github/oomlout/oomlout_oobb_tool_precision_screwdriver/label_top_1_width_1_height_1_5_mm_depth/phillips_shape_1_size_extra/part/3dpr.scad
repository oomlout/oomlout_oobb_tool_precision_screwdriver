$fn = 50;


union() {
	difference() {
		union() {
			cylinder(h = 1.5000000000, r = 6.5000000000);
			rotate_extrude(angle = 360) {
				translate(v = [6.5000000000, 0, 0]) {
					circle(r = 1.5000000000);
				}
			}
		}
		union() {
			translate(v = [-25.0000000000, -25.0000000000, -50]) {
				cube(size = [50, 50, 50]);
			}
			#translate(v = [-3.0000000000, -3.7500000000, 0.5000000000]) {
				cube(size = [6, 1.5000000000, 1]);
			}
			#translate(v = [-0.7500000000, -6.0000000000, 0.5000000000]) {
				cube(size = [1.5000000000, 6, 1]);
			}
			#translate(v = [0, 4, 0.5000000000]) {
				linear_extrude(height = 1) {
					text(font = "SegoiUI:Bold", halign = "center", size = 4.5000000000, text = "1", valign = "center");
				}
			}
		}
	}
	union() {
		translate(v = [0, 0, -6]) {
			linear_extrude(height = 6) {
				polygon(points = [[3.8658550000, 0.0000000000], [1.9329275000, 3.3479286373], [-1.9329275000, 3.3479286373], [-3.8658550000, 0.0000000000], [-1.9329275000, -3.3479286373], [1.9329275000, -3.3479286373]]);
			}
		}
	}
}