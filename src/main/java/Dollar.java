public class Dollar extends Money
{
    private String currency;
    public Dollar(int amount, String currency)
    {
        super(amount, currency);
    }

    public Money times(int multiplier)
    {
        return Money.dollar(amount * multiplier);
    }
}
