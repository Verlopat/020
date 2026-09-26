// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;
import "@openzeppelin/contracts/access/AccessControl.sol";
contract FairnessRegulator is AccessControl{
 bytes32 public constant REGULATOR_ROLE=keccak256("REGULATOR_ROLE");
 uint256 public maxGiniBps;uint256 public minShareBps;
 constructor(address admin,uint256 g,uint256 m){_grantRole(DEFAULT_ADMIN_ROLE,admin);_grantRole(REGULATOR_ROLE,admin);maxGiniBps=g;minShareBps=m;}
 function withinGini(uint256 g) public view returns(bool){return g<=maxGiniBps;}
 function floor(uint256 matching,uint256 projects) public view returns(uint256){return projects==0?0:matching*minShareBps/(10000*projects);}
}
