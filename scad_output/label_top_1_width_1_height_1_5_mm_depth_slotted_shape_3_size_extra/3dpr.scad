$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -0.7500000000]) {
			cylinder(h = 1.5000000000, r = 8.0000000000);
		}
		translate(v = [0, 0, -6]) {
			linear_extrude(height = 6) {
				polygon(points = [[3.8658550000, 0.0000000000], [1.9329275000, 3.3479286373], [-1.9329275000, 3.3479286373], [-3.8658550000, 0.0000000000], [-1.9329275000, -3.3479286373], [1.9329275000, -3.3479286373]]);
			}
		}
	}
	union() {
		#translate(v = [-4.0000000000, -4.0000000000, -0.2500000000]) {
			cube(size = [8, 2, 1]);
		}
		#translate(v = [0, 4.5000000000, -0.2500000000]) {
			linear_extrude(height = 1) {
				text(font = "SegoiUI:Bold", halign = "center", size = 4.5000000000, text = "3", valign = "center");
			}
		}
	}
}