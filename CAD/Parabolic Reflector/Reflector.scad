include <2dgraphing.scad>
function f(x) = 2.25-(x*x)/9;

module dish() {
 rotate([0,180,180]) 2dgraph([0.075,4.5],0.1,3);
}
rotate_extrude($fn=6) dish();