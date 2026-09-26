// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;
import "forge-std/Test.sol";
import "../contracts/ARQFFunding.sol";
contract ARQFFundingTest is Test{
 ARQFFunding f;address admin=address(1);
 function setUp()public{f=new ARQFFunding(admin);}
 function testRoundAndAllocation()public{vm.startPrank(admin);f.createRound(1,1000,2);f.setRandomness(1,7);f.recordAllocation(1,0,500);f.finalize(1);vm.stopPrank();(,,,bool done)=f.rounds(1);assertTrue(done);assertEq(f.allocation(1,0),500);}
 function testOnlyRole()public{vm.expectRevert();f.createRound(2,1,1);}
 function testFuzzAllocation(uint256 p,uint256 amount)public{vm.assume(p<2);vm.prank(admin);f.createRound(3,1,2);vm.prank(admin);f.recordAllocation(3,p,amount);assertEq(f.allocation(3,p),amount);}
}
