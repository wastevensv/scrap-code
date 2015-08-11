$fn = 30;
module leg(h, ro, ri, rot) {
    rotate(a = rot) {
        translate([0,0,5]) linear_extrude(height=h) {
            difference(){
                circle(r=ro);
                circle(r=ri);
            };
        };
    };
};
union() {
    union() {
        leg(20,10,5,[30,30,0]);
        leg(20,10,5,[150,-30,0]);
        leg(20,10,5,[270,0,-30]);
        leg(20,10,5,[0,270,0]);
    };
    sphere(r=12);
};