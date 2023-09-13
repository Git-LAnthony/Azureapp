# Copyright (c) HashiCorp, Inc.
# SPDX-License-Identifier: MPL-2.0

terraform {
  cloud {
    organization = "ResumeApp"

    workspaces {
      name = "azureresumeappworkspace"
    }
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "terragroup" {
  name     = "myTFResourceGroup"
  location = "eastus2"
}
