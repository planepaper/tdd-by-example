package test;

import main.Dollar;

public class MoneyTest
{
    public void testMultiplication()
    {
        Dollar five = new Dollar(5);
        five.times(2);
        assetEquals(10, five.amount);
    }
}
