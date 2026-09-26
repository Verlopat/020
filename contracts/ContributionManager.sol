// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;
import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/utils/ReentrancyGuard.sol";
contract ContributionManager is AccessControl,ReentrancyGuard{
 bytes32 public constant ROUND_MANAGER_ROLE=keccak256("ROUND_MANAGER_ROLE");
 mapping(uint256=>mapping(address=>mapping(uint256=>uint256))) public contributions;
 mapping(uint256=>uint256) public roundTotals;
 constructor(address admin){_grantRole(DEFAULT_ADMIN_ROLE,admin);_grantRole(ROUND_MANAGER_ROLE,admin);}
 function contribute(uint256 roundId,uint256 projectId) external payable nonReentrant{require(msg.value>0,"zero");contributions[roundId][msg.sender][projectId]+=msg.value;roundTotals[roundId]+=msg.value;}
}
