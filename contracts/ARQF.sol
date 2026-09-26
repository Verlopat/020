// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;
contract ARQF {
    struct Contribution{address contributor;uint256 projectId;uint256 amount;}
    struct Round{uint64 start;uint64 end;uint256 matchingPool;bool finalized;}
    uint256 public roundCount; address public owner;
    mapping(uint256=>Round) public rounds; mapping(uint256=>Contribution[]) private contributions; mapping(uint256=>bytes32) public randomnessRequest;
    error Unauthorized(); error InvalidRound(); error ClosedRound(); error ZeroAmount();
    event RoundCreated(uint256 indexed id,uint256 pool,uint64 start,uint64 end);
    event ContributionMade(uint256 indexed id,uint256 indexed project,address indexed contributor,uint256 amount);
    event RandomnessRequested(uint256 indexed id,bytes32 requestId); event RoundFinalized(uint256 indexed id);
    modifier onlyOwner(){if(msg.sender!=owner)revert Unauthorized();_;}
    constructor(){owner=msg.sender;}
    function createRound(uint256 pool,uint64 start,uint64 end) external onlyOwner returns(uint256 id){require(end>start,"bad window");id=++roundCount;rounds[id]=Round(start,end,pool,false);emit RoundCreated(id,pool,start,end);}
    function contribute(uint256 id,uint256 project) external payable{Round memory r=rounds[id];if(r.start==0)revert InvalidRound();if(r.finalized||block.timestamp<r.start||block.timestamp>r.end)revert ClosedRound();if(msg.value==0)revert ZeroAmount();contributions[id].push(Contribution(msg.sender,project,msg.value));emit ContributionMade(id,project,msg.sender,msg.value);}
    function contributionCount(uint256 id)external view returns(uint256){return contributions[id].length;}
    function contributionAt(uint256 id,uint256 i)external view returns(Contribution memory){return contributions[id][i];}
    function recordRandomnessRequest(uint256 id,bytes32 requestId)external onlyOwner{if(rounds[id].finalized)revert ClosedRound();randomnessRequest[id]=requestId;emit RandomnessRequested(id,requestId);}
    function finalize(uint256 id)external onlyOwner{if(rounds[id].start==0)revert InvalidRound();rounds[id].finalized=true;emit RoundFinalized(id);}
}
