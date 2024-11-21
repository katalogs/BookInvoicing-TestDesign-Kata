> This kata is used to train refactoring test inputs with tests data builders.  
> For more information, see [this learning hour](https://sammancoaching.org/learning_hours/test_design/test_data_builders.html)

# Test data builders kata 

We own a company that sells Books on-line in various cities around the world.
To manage our purchases, we have developed an internal system that has two
portals:

#### 1. Customer Portal

This portal, provides our customers with features allowing them to search for
and purchase books.

The purchase workflow is as follows:
1. Customers add the books they want to purchase to a basket.
2. They then checkout their basket.
3. Upon checkout, our system should generate an invoice. The invoice should
   have the following properties:
    1. Tax rates and tax reduction rules should be applied for each item in
       the basket
    2. The total amount of the invoice should be the sum of the amount of all
       books (after tax) in the basket
    3. The currency of the invoice is the same currency as the respective
       country
4.The Invoice is sent to the customer, and a copy of it is saved in our
   repository for future reference

>Tip: It is important to note that each country has its own tax rates and tax
reduction rules. You can find a table of those rules below.

#### 2. Reporting Portal

The second portal is used by administrators to generate reports of the sales
around the world.

The report should include the following:
1. Accumulative sum of all the issued invoices' amount
2. The count of processed invoices
3. The currency of the report should be in USD

### Countries, Currencies, Language, Tax Rates, and Tax Reduction Rules

| Country       | Currency          | Language  | Exchange Rate to USD  | Tax Rate | Tax Reduction Rules                              |
| :-------------|:-----------------:| :--------:| :--------------------:|:--------:|:------------------------------------------------:|
| USA           | USD               | English   | 1.0                   | 15%      | Reduction by 2% on Novels                        |  
| France        | Euro              | French    | 1.14                  | 25%      | No Reduction on taxes                            |
| UK            | Pound Sterling    | English   | 1.27                  | 20%      | Reduction by 7% on Novels                        |
| Spain         | Euro              | Spanish   | 1.14                  | 10%      | Removed taxes on all foreign language books      |  
| China         | Renminbi          | Mandarin  | 0.15                  | 35%      | Removed taxes on all foreign language books      |
| Japan         | YEN               | Japanese  | 0.0093                | 30%      | No Reduction on taxes                            |
| Australia     | Australian Dollar | English   | 0.70                  | 13%      | No Reduction on taxes                            |     
| Germany       | Euro              | German    | 1.14                  | 22%      | Dropped to 5% on books written by German Authors |


## Versions

This kata includes the following versions:

- [c#](./csharp/README.md)
- [PHP](./php/README.md)
- [python](./python/README.md)
- [typescript](./typescript/README.md)

## Credits

This kata is a backport from [Mikado Method and Test Data Builders Kata](https://github.com/murex/mikado-testbuilders-kata) under the [MIT Licence](./LICENSE).

Tests are included in this version to have a training focused on the usage of the [Tests data builders](http://www.natpryce.com/articles/000714.html), removing the code discovery needs.

Thanks to [Philippe Bourgau](https://github.com/philou) and [the whole team of contributors](https://github.com/murex/mikado-testbuilders-kata/graphs/contributors) for their work. 
