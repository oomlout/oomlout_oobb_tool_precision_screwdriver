$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -0.7500000000]) {
			cylinder(h = 1.5000000000, r = 8.0000000000);
		}
		translate(v = [0, 0, -6]) {
			linear_extrude(height = 6) {
				polygon(points = [[3.8408550000, 0.0000000000], [1.9204275000, 3.3262780023], [-1.9204275000, 3.3262780023], [-3.8408550000, 0.0000000000], [-1.9204275000, -3.3262780023], [1.9204275000, -3.3262780023]]);
			}
		}
	}
	union() {
		#translate(v = [-4.0000000000, -3.0000000000, 0.2500000000]) {
			cube(size = [8, 2, 0.5000000000]);
		}
		#translate(v = [0, 4, 0.2500000000]) {
			linear_extrude(height = 0.5000000000) {
				text(font = "SegoiUI:Bold", halign = "center", size = 4.5000000000, text = "4", valign = "center");
			}
		}
	}
}