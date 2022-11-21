# Cloud-Billing-and-Usage-Dashboard
This Dashboard gives insight into the Cloud Billing Costs and Usage.

# Dashboard Overview
This code implements a dataset using standard and detailed billing exports and creates necessary BQ views.

Datastudio template report/dashboard is used to show prebuilt reports based on the BQ views.

You have an option to not create views and use a custom query.


## Environment set-up

You can set-up the right python environment as follows:
```
 git clone https://github.com/meghabedi/Cloud-Billing-and-Usage-Dashboard.git
 cd Cloud-Billing-and-Usage-Dashboard
 rm -rf dash-env
 pip install virtualenv
 virtualenv dash-env
 source dash-env/bin/activate
 pip install -r requirements.txt
```
This step includes the following:
- Install Python local env
- Launch local env
- Install dependencies

## There are 2 options for dashboard generation
For dashboard with BQ views:
```
python dashboard_gen.py -pr <project id> -se <standard billing ds> -de <detailed billing ds> -bb <billboard_ds>
```

For dashboard with Custom SQL:
```
python dashboard.py
```
Copy paste the billing_export.sql in the Data Source. Enable the data range parameter just below the the custom query.


## Create billing dataset
 -se standard billing export dataset
 -de detailed billing export dataset 
 -bb billboard dataset to be created


Explore the datastudio dashboard and explore your billing by clicking the link which was the output of the script

#

# If you want to remove this app from your project for any reason, use clean


## Clean up ( optional for removing BQ Billboard Views )

```

python dashboard_gen.py -pr <project id> -se <standard billing ds> -de <detailed billing ds> -bb <billboard_ds> -clean yes

```

dashboard_gen_public.py code will generate the dashboard with data source containing Public dataset for Cloud Billing and Usage information. 
