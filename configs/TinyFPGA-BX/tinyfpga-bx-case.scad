

module dsub() {
    $fn=20;

    function db_conn_table(idx) =
    // b, d, f, k
    idx == "db9F" ? [12.50,11.10,6.53,2.11] :
    idx == "db9R" ? [12.50,11.10,5.72,3.35] :
    idx == "db15F" ? [16.66,15.27,6.53,2.11] :
    idx == "db15R" ? [16.66,15.27,5.72,3.35] :
    idx == "db25F" ? [23.52,22.15,6.53,2.11] :
    idx == "db25R" ? [23.52,22.0,6.0,3.35] :
    idx == "db37F" ? [31.75,29.54,6.53,2.11] :
    idx == "db37R" ? [31.75,29.54,5.72,3.35] :
    idx == "db50F" ? [30.56,29.19,7.93,2.11] :
    idx == "db50R" ? [30.56,28.17,7.06,3.35] :
    "Error";

    conn = "db25R";

    conn_dimensions = db_conn_table(conn);
    if(conn_dimensions == "Error") {
    echo(str("connector not found"));
    }

    b = db_conn_table(conn)[0];
    d = db_conn_table(conn)[1];
    f = db_conn_table(conn)[2];
    k = db_conn_table(conn)[3];

    //b = 16.66;
    //d = 14.40;
    //f = 5.72;
    //k = 3.35;

    cut_angle = 10;
    mounting_hole = 3.05;

    hull(){
    //Upper Left
    translate([-(d-k),(f-k),0])
    cylinder(1, d=k, center=false);
    //Upper Right
    translate([(d-k),(f-k),0])
    cylinder(h=1, d=k);
    //Lower Left
    translate([-(d-k)+cos(cut_angle),-(f-k),0])
    cylinder(h=1, d=k);
    //Lower Right
    translate([(d-k)-cos(cut_angle),-(f-k),0])
    cylinder(h=1, d=k);
    }

    // Mounting Holes
    translate([-b,0,0])
    cylinder(h=1, d=mounting_hole);
    translate([b,0,0])
    cylinder(h=1, d=mounting_hole);
}



difference() {
    translate([0, 19, 0]) {
        cube([58, 40, 17], center=true);
    }

    translate([0, 19, 2]) {
        cube([58-2, 40-2, 17], center=true);
    }

    rotate([90, 0, 0]) {
        dsub();
    }
    translate([-26, 5, -5]) {
        rotate([90, 0, 0]) {
            cylinder(d=2, h=10, $fn=32);
        }
    }
    translate([6, 40, 6]) {
        cube([15, 15, 9], center=true);
    }
}

rotate([180, 0, 0]) {

    difference() {
        union() {
            translate([0, 29, 8]) {
                cube([58, 40, 1], center=true);
            }
            translate([0, 29, 8-1]) {
                cube([58-2, 40-2, 1], center=true);
            }
        }
        translate([0, 38.5, 8]) {
            cube([37, 5, 10], center=true);
        }
    }


}









