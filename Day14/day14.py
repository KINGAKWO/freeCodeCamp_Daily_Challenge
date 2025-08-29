def burn_candles(candles, makeNew):
    total_burned = 0
    leftovers = 0

    while candles > 0:
        # Burn current candles
        total_burned += candles
        leftovers += candles
        candles = 0

        # Recycle leftovers into new candles
        new_candles = leftovers // makeNew
        leftovers = leftovers % makeNew
        candles += new_candles

    return total_burned
