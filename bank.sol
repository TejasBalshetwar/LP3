// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.6.0;

contract MyBank {
    mapping(address => uint256) private _balances;
    // With this mapping in place we then built a function to track a user’s current balance.
    address public owner;
    event LogDepositeMade(address accountHoder, uint256 amount);

    constructor() public {
        owner = msg.sender;
    }

    function deposite() public payable returns (string memory) {
        _balances[msg.sender] += msg.value;
        return "Deposit success";
    }

    function withdraw(uint256 withdrawAmount) public returns (uint256) {
        require(_balances[msg.sender] >= withdrawAmount);
        _balances[msg.sender] -= withdrawAmount;
        msg.sender.transfer(withdrawAmount);
        return _balances[msg.sender];
    }

    function viewBalance() public view returns (uint256) {
        return _balances[msg.sender];
    }
}