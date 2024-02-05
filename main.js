
import { Transfer } from "./lib/js/parentModule.js";

const hohmannRatio = 11.94
const biellipticRatio = 15.58
const radiiRatio = 1

// Each case will call the 'Transfer class'
switch (radiiRatio) {

  case (radiiRatio < hohmannRatio):
    {
      // Hohmann Transfer call goes HERE
      console.log("Hohmann Transfer!");
      break;
    }

  case (radiiRatio < biellipticRatio && radiiRatio >= hohmannRatio):
    {
      // Bi-Parabolic Transfer call goes HERE
      console.log("Bi-Parabolic Transfer");
 
    }

  case (radiiRatio >= biellipticRatio):
    {
      // Bi-Elliptic Transfer call goes HERE
      console.log("Bielliptic Transfer");
    }

  default:
    {
      // throw new Error(`No orbital transfer was selected with radiiRati: ${radiiRatio}`)
      console.log("no orbit selected")
    }
}