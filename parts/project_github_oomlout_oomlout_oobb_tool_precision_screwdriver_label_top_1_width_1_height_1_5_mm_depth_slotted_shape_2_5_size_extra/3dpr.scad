$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -0.7500000000]) {
			cylinder(h = 1.5000000000, r = 9.0000000000);
		}
		translate(v = [0, 0, -6]) {
			linear_extrude(height = 6) {
				polygon(points = [[3.1658550000, 0.0000000000], [1.5829275000, 2.7417108547], [-1.5829275000, 2.7417108547], [-3.1658550000, 0.0000000000], [-1.5829275000, -2.7417108547], [1.5829275000, -2.7417108547]]);
			}
		}
	}
	union() {
		#translate(v = [-4.0000000000, -4.2500000000, -0.2500000000]) {
			cube(size = [8, 2.5000000000, 1]);
		}
		#translate(v = [0, 5, -0.2500000000]) {
			linear_extrude(height = 1) {
				text(font = "SegoiUI:Bold", halign = "center", size = 3.5000000000, text = "2.5", valign = "center");
			}
		}
	}
}