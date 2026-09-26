// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;
import "forge-std/Script.sol";
import "../contracts/ARQFFunding.sol";
import "../contracts/ContributionManager.sol";
import "../contracts/ARQFGovernance.sol";
import "../contracts/FairnessRegulator.sol";
contract Deploy is Script {
 function run() external returns(ARQFFunding funding,ContributionManager contributions,ARQFGovernance governance,FairnessRegulator regulator){
  uint256 key=vm.envUint("PRIVATE_KEY");address admin=vm.addr(key);vm.startBroadcast(key);
  funding=new ARQFFunding(admin);contributions=new ContributionManager(admin);governance=new ARQFGovernance(admin);regulator=new FairnessRegulator(admin,governance.maxGiniBps(),governance.minProjectShareBps());
  vm.stopBroadcast();
 }
}
