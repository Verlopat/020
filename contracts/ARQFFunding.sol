// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;
import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/utils/ReentrancyGuard.sol";
contract ARQFFunding is AccessControl,ReentrancyGuard{
 bytes32 public constant ROUND_ROLE=keccak256("ROUND_ROLE");
 struct Round{uint256 matchingPool;uint256 projects;uint256 randomness;bool finalized;}
 mapping(uint256=>Round) public rounds;mapping(uint256=>mapping(uint256=>uint256)) public allocation;
 constructor(address admin){_grantRole(DEFAULT_ADMIN_ROLE,admin);_grantRole(ROUND_ROLE,admin);}
 function createRound(uint256 id,uint256 pool,uint256 projects) external onlyRole(ROUND_ROLE){require(projects>0,"projects");rounds[id]=Round(pool,projects,0,false);}
 function setRandomness(uint256 id,uint256 word) external onlyRole(ROUND_ROLE){require(!rounds[id].finalized,"finalized");rounds[id].randomness=word;}
 function recordAllocation(uint256 id,uint256 project,uint256 amount) external onlyRole(ROUND_ROLE){require(project<rounds[id].projects,"project");allocation[id][project]=amount;}
 function finalize(uint256 id) external onlyRole(ROUND_ROLE){require(rounds[id].randomness!=0,"randomness");rounds[id].finalized=true;}
}
