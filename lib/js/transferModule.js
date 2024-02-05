
"use strict";

class Transfer {
  //compile transfer data to here for delta V calculation based on pre-established clusters of rocket bodies.

  //Some objects that may be needed:
  // 1. orbital details of transfer start
  // 2. orbital details of transfer destination

  constructor(orbitalDatastub1, orbitalDatastub2, type) {
    this.orbitalData1 = orbitalDatastub1;
    this.orbitalData2 = orbitalDatastub2;
    this.type = type;
  }

  get deltaV() {
    return this.calcDeltaV();
  }

  calcDeltaV() {
    if (this.type == "hohmann") {
      hohmannTransfer();
    } else if (this.type == "biparabolic") {
      biParabolicTransfer();
    } else if (this.type == "bielliptic") {
      biEllipticTransfer();
    }
  }

  static hohmannTransfer() {
    //hohmann transfer math goes here
    // returns deltaV (int)
    
  }

  static biParabolicTransfer() {
    //bi parabolic transfer math goes here
    // returns deltaV (int)
  }

  static biEllipticTransfer() {
    // bi elliptic transfer math goes here
    // returns deltaV (int)
  }
}

export default Transfer;