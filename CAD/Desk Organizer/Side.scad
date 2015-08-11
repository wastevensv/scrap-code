thickness = 0.1875;
module side() {
    difference() {
        cube([20,30,thickness]); // Main board
        for(h = [1,6,11,16,21] ) {
            translate([0,h,-1]) cube([10,thickness,2+thickness]); // Shelf Cuts
        }
        translate([15,15,-1]) cube([thickness,15,2+thickness]); // Back Cut
    }
}

projection() side();