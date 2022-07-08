abstract public class Money
{
    protected int amount;
    protected String currency;

    public Money(int amount, String currency)
    {
        this.amount = amount;
        this.currency = currency;
    }

    abstract Money times(int multiplier);

    public boolean equals(Object object)
    {
        Money money = (Money) object;
        return amount == money.amount
                && getClass().equals(money.getClass());
    }

    static Money dollar(int amount)
    {
        return new Dollar(amount, "USD");
    }

    static Money franc(int amount)
    {
        return new Franc(amount, "CHF");
    }

    String currency()
    {
        return currency;
    }
}
