# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: market.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cmarket.proto\"+\n\nSellerInfo\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0c\n\x04uuid\x18\x02 \x01(\t\"\xad\x01\n\x04Item\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x13\n\x0bproductName\x18\x02 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x03 \x01(\t\x12\x10\n\x08quantity\x18\x04 \x01(\x05\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x15\n\rsellerAddress\x18\x06 \x01(\t\x12\x14\n\x0cpricePerUnit\x18\x07 \x01(\x01\x12\x13\n\x06rating\x18\x08 \x01(\x01H\x00\x88\x01\x01\x42\t\n\x07_rating\"9\n\x15RegisterSellerRequest\x12 \n\x0bseller_info\x18\x01 \x01(\x0b\x32\x0b.SellerInfo\"k\n\x16RegisterSellerResponse\x12.\n\x06status\x18\x01 \x01(\x0e\x32\x1e.RegisterSellerResponse.Status\"!\n\x06Status\x12\x0b\n\x07SUCCESS\x10\x00\x12\n\n\x06\x46\x41ILED\x10\x01\"H\n\x0fSellItemRequest\x12 \n\x0bseller_info\x18\x01 \x01(\x0b\x32\x0b.SellerInfo\x12\x13\n\x04item\x18\x02 \x01(\x0b\x32\x05.Item\"p\n\x10SellItemResponse\x12(\n\x06status\x18\x01 \x01(\x0e\x32\x18.SellItemResponse.Status\x12\x0f\n\x07item_id\x18\x02 \x01(\x05\"!\n\x06Status\x12\x0b\n\x07SUCCESS\x10\x00\x12\n\n\x06\x46\x41ILED\x10\x01\"o\n\x11UpdateItemRequest\x12 \n\x0bseller_info\x18\x01 \x01(\x0b\x32\x0b.SellerInfo\x12\x0f\n\x07item_id\x18\x02 \x01(\x05\x12\x11\n\tnew_price\x18\x03 \x01(\x01\x12\x14\n\x0cnew_quantity\x18\x04 \x01(\x05\"c\n\x12UpdateItemResponse\x12*\n\x06status\x18\x01 \x01(\x0e\x32\x1a.UpdateItemResponse.Status\"!\n\x06Status\x12\x0b\n\x07SUCCESS\x10\x00\x12\n\n\x06\x46\x41ILED\x10\x01\"F\n\x11\x44\x65leteItemRequest\x12 \n\x0bseller_info\x18\x01 \x01(\x0b\x32\x0b.SellerInfo\x12\x0f\n\x07item_id\x18\x02 \x01(\x05\"c\n\x12\x44\x65leteItemResponse\x12*\n\x06status\x18\x01 \x01(\x0e\x32\x1a.DeleteItemResponse.Status\"!\n\x06Status\x12\x0b\n\x07SUCCESS\x10\x00\x12\n\n\x06\x46\x41ILED\x10\x01\"=\n\x19\x44isplaySellerItemsRequest\x12 \n\x0bseller_info\x18\x01 \x01(\x0b\x32\x0b.SellerInfo\"\x89\x01\n\x1a\x44isplaySellerItemsResponse\x12\x32\n\x06status\x18\x01 \x01(\x0e\x32\".DisplaySellerItemsResponse.Status\x12\x14\n\x05items\x18\x02 \x03(\x0b\x32\x05.Item\"!\n\x06Status\x12\x0b\n\x07SUCCESS\x10\x00\x12\n\n\x06\x46\x41ILED\x10\x01\"\x1c\n\tBuyerInfo\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\"\x93\x01\n\x11SearchItemRequest\x12\x10\n\x08itemName\x18\x01 \x01(\t\x12-\n\x08\x63\x61tegory\x18\x02 \x01(\x0e\x32\x1b.SearchItemRequest.Category\"=\n\x08\x43\x61tegory\x12\x0f\n\x0b\x45LECTRONICS\x10\x00\x12\x0b\n\x07\x46\x41SHION\x10\x01\x12\n\n\x06OTHERS\x10\x02\x12\x07\n\x03\x41NY\x10\x03\"*\n\x12SearchItemResponse\x12\x14\n\x05items\x18\x01 \x03(\x0b\x32\x05.Item\"H\n\x0e\x42uyItemRequest\x12\x0e\n\x06itemId\x18\x01 \x01(\x05\x12\x10\n\x08quantity\x18\x02 \x01(\x05\x12\x14\n\x0c\x62uyerAddress\x18\x03 \x01(\t\"]\n\x0f\x42uyItemResponse\x12\'\n\x06status\x18\x01 \x01(\x0e\x32\x17.BuyItemResponse.Status\"!\n\x06Status\x12\x0b\n\x07SUCCESS\x10\x00\x12\n\n\x06\x46\x41ILED\x10\x01\"<\n\x14\x41\x64\x64ToWishListRequest\x12\x0e\n\x06itemId\x18\x01 \x01(\x05\x12\x14\n\x0c\x62uyerAddress\x18\x02 \x01(\t\"i\n\x15\x41\x64\x64ToWishListResponse\x12-\n\x06status\x18\x01 \x01(\x0e\x32\x1d.AddToWishListResponse.Status\"!\n\x06Status\x12\x0b\n\x07SUCCESS\x10\x00\x12\n\n\x06\x46\x41ILED\x10\x01\"G\n\x0fRateItemRequest\x12\x0e\n\x06itemId\x18\x01 \x01(\x05\x12\x14\n\x0c\x62uyerAddress\x18\x02 \x01(\t\x12\x0e\n\x06rating\x18\x03 \x01(\x05\"_\n\x10RateItemResponse\x12(\n\x06status\x18\x01 \x01(\x0e\x32\x18.RateItemResponse.Status\"!\n\x06Status\x12\x0b\n\x07SUCCESS\x10\x00\x12\n\n\x06\x46\x41ILED\x10\x01\x32\x96\x04\n\rMarketService\x12\x41\n\x0eRegisterSeller\x12\x16.RegisterSellerRequest\x1a\x17.RegisterSellerResponse\x12/\n\x08SellItem\x12\x10.SellItemRequest\x1a\x11.SellItemResponse\x12\x35\n\nUpdateItem\x12\x12.UpdateItemRequest\x1a\x13.UpdateItemResponse\x12\x35\n\nDeleteItem\x12\x12.DeleteItemRequest\x1a\x13.DeleteItemResponse\x12M\n\x12\x44isplaySellerItems\x12\x1a.DisplaySellerItemsRequest\x1a\x1b.DisplaySellerItemsResponse\x12\x35\n\nSearchItem\x12\x12.SearchItemRequest\x1a\x13.SearchItemResponse\x12,\n\x07\x42uyItem\x12\x0f.BuyItemRequest\x1a\x10.BuyItemResponse\x12>\n\rAddToWishList\x12\x15.AddToWishListRequest\x1a\x16.AddToWishListResponse\x12/\n\x08RateItem\x12\x10.RateItemRequest\x1a\x11.RateItemResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'market_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_SELLERINFO']._serialized_start=16
  _globals['_SELLERINFO']._serialized_end=59
  _globals['_ITEM']._serialized_start=62
  _globals['_ITEM']._serialized_end=235
  _globals['_REGISTERSELLERREQUEST']._serialized_start=237
  _globals['_REGISTERSELLERREQUEST']._serialized_end=294
  _globals['_REGISTERSELLERRESPONSE']._serialized_start=296
  _globals['_REGISTERSELLERRESPONSE']._serialized_end=403
  _globals['_REGISTERSELLERRESPONSE_STATUS']._serialized_start=370
  _globals['_REGISTERSELLERRESPONSE_STATUS']._serialized_end=403
  _globals['_SELLITEMREQUEST']._serialized_start=405
  _globals['_SELLITEMREQUEST']._serialized_end=477
  _globals['_SELLITEMRESPONSE']._serialized_start=479
  _globals['_SELLITEMRESPONSE']._serialized_end=591
  _globals['_SELLITEMRESPONSE_STATUS']._serialized_start=370
  _globals['_SELLITEMRESPONSE_STATUS']._serialized_end=403
  _globals['_UPDATEITEMREQUEST']._serialized_start=593
  _globals['_UPDATEITEMREQUEST']._serialized_end=704
  _globals['_UPDATEITEMRESPONSE']._serialized_start=706
  _globals['_UPDATEITEMRESPONSE']._serialized_end=805
  _globals['_UPDATEITEMRESPONSE_STATUS']._serialized_start=370
  _globals['_UPDATEITEMRESPONSE_STATUS']._serialized_end=403
  _globals['_DELETEITEMREQUEST']._serialized_start=807
  _globals['_DELETEITEMREQUEST']._serialized_end=877
  _globals['_DELETEITEMRESPONSE']._serialized_start=879
  _globals['_DELETEITEMRESPONSE']._serialized_end=978
  _globals['_DELETEITEMRESPONSE_STATUS']._serialized_start=370
  _globals['_DELETEITEMRESPONSE_STATUS']._serialized_end=403
  _globals['_DISPLAYSELLERITEMSREQUEST']._serialized_start=980
  _globals['_DISPLAYSELLERITEMSREQUEST']._serialized_end=1041
  _globals['_DISPLAYSELLERITEMSRESPONSE']._serialized_start=1044
  _globals['_DISPLAYSELLERITEMSRESPONSE']._serialized_end=1181
  _globals['_DISPLAYSELLERITEMSRESPONSE_STATUS']._serialized_start=370
  _globals['_DISPLAYSELLERITEMSRESPONSE_STATUS']._serialized_end=403
  _globals['_BUYERINFO']._serialized_start=1183
  _globals['_BUYERINFO']._serialized_end=1211
  _globals['_SEARCHITEMREQUEST']._serialized_start=1214
  _globals['_SEARCHITEMREQUEST']._serialized_end=1361
  _globals['_SEARCHITEMREQUEST_CATEGORY']._serialized_start=1300
  _globals['_SEARCHITEMREQUEST_CATEGORY']._serialized_end=1361
  _globals['_SEARCHITEMRESPONSE']._serialized_start=1363
  _globals['_SEARCHITEMRESPONSE']._serialized_end=1405
  _globals['_BUYITEMREQUEST']._serialized_start=1407
  _globals['_BUYITEMREQUEST']._serialized_end=1479
  _globals['_BUYITEMRESPONSE']._serialized_start=1481
  _globals['_BUYITEMRESPONSE']._serialized_end=1574
  _globals['_BUYITEMRESPONSE_STATUS']._serialized_start=370
  _globals['_BUYITEMRESPONSE_STATUS']._serialized_end=403
  _globals['_ADDTOWISHLISTREQUEST']._serialized_start=1576
  _globals['_ADDTOWISHLISTREQUEST']._serialized_end=1636
  _globals['_ADDTOWISHLISTRESPONSE']._serialized_start=1638
  _globals['_ADDTOWISHLISTRESPONSE']._serialized_end=1743
  _globals['_ADDTOWISHLISTRESPONSE_STATUS']._serialized_start=370
  _globals['_ADDTOWISHLISTRESPONSE_STATUS']._serialized_end=403
  _globals['_RATEITEMREQUEST']._serialized_start=1745
  _globals['_RATEITEMREQUEST']._serialized_end=1816
  _globals['_RATEITEMRESPONSE']._serialized_start=1818
  _globals['_RATEITEMRESPONSE']._serialized_end=1913
  _globals['_RATEITEMRESPONSE_STATUS']._serialized_start=370
  _globals['_RATEITEMRESPONSE_STATUS']._serialized_end=403
  _globals['_MARKETSERVICE']._serialized_start=1916
  _globals['_MARKETSERVICE']._serialized_end=2450
# @@protoc_insertion_point(module_scope)