


module wt32eth0() {

    translate([-22/2+4.5, 0, 7]) {
        cube([22, 16, 14], center=true);
    }

    translate([-55/2, 0, -1.7/2]) {
        cube([55, 25.5, 1.7], center=true);
    }

}

module wt32eth0_diff() {

    translate([-22/2+4.5, 0, 7]) {
        cube([22, 16, 14], center=true);
    }

    translate([-55/2, 0, -1.7/2]) {
        cube([55, 25.5, 1.7], center=true);
    }
    translate([-47/2, 0, -1.7/2]) {
        cube([47, 25.5-1.5, 8], center=true);
    }
    translate([-33/2-14, 0, 19/2]) {
        cube([33, 25.5, 19], center=true);
    }
}


difference() {
    translate([-28, 0, 9]) {
        cube([63, 28, 30], center=true);
    }
    translate([-28-1.1, 0, 10]) {
        cube([63-2, 28-2, 30-4], center=true);
    }
    wt32eth0_diff();

    for (i = [1: 9]){
        hull() {
            translate([-i*6, 0, 20]) {
                rotate([90, 0, 0]) {
                    cylinder(d=2, h=40, $fn=32, center=true);
                }
            }
            translate([-i*6+5, 0, 5]) {
                rotate([90, 90, 0]) {
                    cylinder(d=2, h=40, $fn=32, center=true);
                }
            }
        }
    }

}

difference() {
    union() {
        translate([-80, 0, 9]) {
            cube([1, 28, 30], center=true);
        }
        translate([-80+1, 0, 10]) {
            cube([2, 28-2, 30-4], center=true);
        }
    }
    translate([-80, 0, 22.5]) {
        cube([10, 9, 5], center=true);
    }
}

