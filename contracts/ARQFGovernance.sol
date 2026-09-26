// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;
import "@openzeppelin/contracts/access/AccessControl.sol";
contract ARQFGovernance is AccessControl{
 bytes32 public constant PARAMETER_ROLE=keccak256("PARAMETER_ROLE");
 uint256 public maxGiniBps=3500;uint256 public minProjectShareBps=50;uint256 public adaptiveStrengthBps=7500;
 constructor(address admin){_grantRole(DEFAULT_ADMIN_ROLE,admin);_grantRole(PARAMETER_ROLE,admin);}
 function setParameters(uint256 g,uint256 m,uint256 s) external onlyRole(PARAMETER_ROLE){require(g<=10000&&m<=10000&&s<=10000,"range");maxGiniBps=g;minProjectShareBps=m;adaptiveStrengthBps=s;}
}
