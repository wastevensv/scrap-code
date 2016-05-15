union() {
    translate([18,0,5])
    rotate([0,90,0])  cylinder(h=4, r=10);
    difference() {
        cylinder(h=10, r=20);
        cylinder(h=10, r=15);
    }
}