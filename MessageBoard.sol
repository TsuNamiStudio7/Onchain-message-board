// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MessageBoard {
    struct Message {
        address sender;
        string text;
        uint256 timestamp;
    }

    Message[] public messages;

    event NewMessage(address indexed sender, string text, uint256 timestamp);

    function postMessage(string calldata _text) public {
        messages.push(Message(msg.sender, _text, block.timestamp));
        emit NewMessage(msg.sender, _text, block.timestamp);
    }

    function getMessageCount() public view returns (uint256) {
        return messages.length;
    }

    function getMessage(uint256 index) public view returns (address, string memory, uint256) {
        require(index < messages.length, "Invalid index");
        Message memory msgData = messages[index];
        return (msgData.sender, msgData.text, msgData.timestamp);
    }
}
