# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.cloud import bigquery
from google.cloud import billing
from google.api_core.exceptions import PermissionDenied
from google.cloud.exceptions import NotFound
import argparse
import sys
from colorama import Back
from colorama import Style

bq_client = bigquery.Client()
base_url = "https://datastudio.google.com/reporting/create?"
report_part_url = base_url + "c.reportId=afc93bd5-2fd9-4682-a083-0494071cc858"
report_base_url = report_part_url + "&r.reportName=BillingUsage"

std_proj_url = "&ds.ds0.connector=bigQuery&ds.ds0.projectId={}"
std_table_url = "&ds.ds0.type=TABLE&ds.ds0.datasetId={}&ds.ds0.tableId={}"
standard_view_url = std_proj_url + std_table_url

dtl_proj_url = "&ds.ds2.connector=bigQuery&ds.ds2.projectId={}"
dtl_table_url = "&ds.ds2.type=TABLE&ds.ds2.datasetId={}&ds.ds2.tableId={}"
detailed_view_url = dtl_proj_url + dtl_table_url

output_url = report_base_url + standard_view_url

app_version = "2.0"

def generate_datastudio_url():
    print(
        "To view dataset, please click " + Back.GREEN +
        "https://console.cloud.google.com/bigquery", "\n")

    print(Style.RESET_ALL)

    print("To launch datastudio report, please click " + Back.GREEN +
          output_url + "\n")
    print(Style.RESET_ALL)

def main():
    generate_datastudio_url()



# Main entry point
if __name__ == "__main__":
    main()
