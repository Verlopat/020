// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;
import {VRFConsumerBaseV2Plus} from "@chainlink/contracts/src/v0.8/vrf/dev/VRFConsumerBaseV2Plus.sol";
import {VRFV2PlusClient} from "@chainlink/contracts/src/v0.8/vrf/dev/libraries/VRFV2PlusClient.sol";
contract ARQFVRFConsumer is VRFConsumerBaseV2Plus {
    uint256 public immutable subscriptionId; bytes32 public immutable keyHash; uint32 public callbackGasLimit;
    uint16 public requestConfirmations=3; uint32 public numWords=1;
    mapping(uint256=>uint256)public requestToRound; mapping(uint256=>uint256)public roundRandomness;
    event RandomnessRequested(uint256 indexed roundId,uint256 indexed requestId); event RandomnessFulfilled(uint256 indexed roundId,uint256 indexed requestId,uint256 value);
    constructor(address coordinator,uint256 subId,bytes32 hash,uint32 gasLimit)VRFConsumerBaseV2Plus(coordinator){subscriptionId=subId;keyHash=hash;callbackGasLimit=gasLimit;}
    function requestRoundRandomness(uint256 roundId)external onlyOwner returns(uint256 requestId){
        requestId=s_vrfCoordinator.requestRandomWords(VRFV2PlusClient.RandomWordsRequest({keyHash:keyHash,subId:subscriptionId,requestConfirmations:requestConfirmations,callbackGasLimit:callbackGasLimit,numWords:numWords,extraArgs:VRFV2PlusClient._argsToBytes(VRFV2PlusClient.ExtraArgsV1({nativePayment:false}))}));
        requestToRound[requestId]=roundId;emit RandomnessRequested(roundId,requestId);
    }
    function fulfillRandomWords(uint256 requestId,uint256[]calldata randomWords)internal override{uint256 roundId=requestToRound[requestId];roundRandomness[roundId]=randomWords[0];emit RandomnessFulfilled(roundId,requestId,randomWords[0]);}
}
