#LloydsLiving - Bronze - FixFlo v1.0
Generated using [DbSchema](https://dbschema.com)




### LloydsLiving - Bronze - FixFlo v1.0
![img](./LloydsLiving-Bronze-FixFlov1.0.svg)


## Tables

1. [FixFlo.Block](#table%20fixflo.block) 
2. [FixFlo.Contractor](#table%20fixflo.contractor) 
3. [FixFlo.Estate](#table%20fixflo.estate) 
4. [FixFlo.Issue](#table%20fixflo.issue) 
5. [FixFlo.Landlord](#table%20fixflo.landlord) 
6. [FixFlo.Leaseholder](#table%20fixflo.leaseholder) 
7. [FixFlo.Property](#table%20fixflo.property) 
8. [FixFlo.Tenant](#table%20fixflo.tenant) 

## Views

1. [FixFlo.DIM_DATE_VW](#view%20fixflo.dim\_date\_vw) 


### Table FixFlo.Block 
|Idx |Name |Data Type |
|---|---|---|
| &#128270; | Address\_AddressLine1| varchar(8000)  |
| &#128270; | Address\_AddressLine2| varchar(8000)  |
| &#128270; | Address\_Country| varchar(8000)  |
| &#128270; | Address\_County| varchar(8000)  |
| &#128270; | Address\_PostCode| varchar(8000)  |
| &#128270; | Address\_Town| varchar(8000)  |
| &#128270; | AssignedAgent| varchar(8000)  |
| &#128270; | Brand| varchar(8000)  |
| &#128270; | Created| varchar(8000)  |
| &#128270; | EstateId| bigint  |
| &#128270; | ExternalBlockReference| varchar(8000)  |
| &#128270; | ExternalEstateRef| varchar(8000)  |
| &#128270; | ExternalLandlordRef| varchar(8000)  |
| &#128270; | Id| bigint  |
| &#128270; | IngestedUTC| varchar(8000)  |
| &#128270; | IsDeleted| bit  |
| &#128270; | IsStandAlone| bit  |
| &#128270; | KeyReference| varchar(8000)  |
| &#128270; | LandlordId| varchar(8000)  |
| &#128270; | ManagementEndDate| varchar(8000)  |
| &#128270; | ManagementStartDate| varchar(8000)  |
| &#128270; | Name| varchar(8000)  |
| &#128270; | PropertyManager| varchar(8000)  |
| &#128270; | UpdateDate| varchar(8000)  |
| &#128270; | Warranties| varchar(8000)  |
| &#128270; | \_source\_page| bigint  |
| &#128270; | \_meta\_source\_file\_name| varchar(8000)  |
| &#128270; | \_meta\_source\_file\_path| varchar(8000)  |
| &#128270; | \_meta\_raw\_row\_number| int  |
| &#128270; | \_meta\_row\_hash| varchar(8000)  |
| &#128270; | \_meta\_pipeline\_id| varchar(8000)  |
| &#128270; | \_meta\_ingest\_ts| datetime2(26)  |


##### Indexes 
|Type |Name |On |
|---|---|---|
| &#128270;  | ClusteredIndex | ON Address\_AddressLine1|
| &#128270;  | ClusteredIndex | ON Address\_AddressLine2|
| &#128270;  | ClusteredIndex | ON Address\_Country|
| &#128270;  | ClusteredIndex | ON Address\_County|
| &#128270;  | ClusteredIndex | ON Address\_PostCode|
| &#128270;  | ClusteredIndex | ON Address\_Town|
| &#128270;  | ClusteredIndex | ON AssignedAgent|
| &#128270;  | ClusteredIndex | ON Brand|
| &#128270;  | ClusteredIndex | ON Created|
| &#128270;  | ClusteredIndex | ON EstateId|
| &#128270;  | ClusteredIndex | ON ExternalBlockReference|
| &#128270;  | ClusteredIndex | ON ExternalEstateRef|
| &#128270;  | ClusteredIndex | ON ExternalLandlordRef|
| &#128270;  | ClusteredIndex | ON Id|
| &#128270;  | ClusteredIndex | ON IngestedUTC|
| &#128270;  | ClusteredIndex | ON IsDeleted|
| &#128270;  | ClusteredIndex | ON IsStandAlone|
| &#128270;  | ClusteredIndex | ON KeyReference|
| &#128270;  | ClusteredIndex | ON LandlordId|
| &#128270;  | ClusteredIndex | ON ManagementEndDate|
| &#128270;  | ClusteredIndex | ON ManagementStartDate|
| &#128270;  | ClusteredIndex | ON Name|
| &#128270;  | ClusteredIndex | ON PropertyManager|
| &#128270;  | ClusteredIndex | ON UpdateDate|
| &#128270;  | ClusteredIndex | ON Warranties|
| &#128270;  | ClusteredIndex | ON \_source\_page|
| &#128270;  | ClusteredIndex | ON \_meta\_source\_file\_name|
| &#128270;  | ClusteredIndex | ON \_meta\_source\_file\_path|
| &#128270;  | ClusteredIndex | ON \_meta\_raw\_row\_number|
| &#128270;  | ClusteredIndex | ON \_meta\_row\_hash|
| &#128270;  | ClusteredIndex | ON \_meta\_pipeline\_id|
| &#128270;  | ClusteredIndex | ON \_meta\_ingest\_ts|



### Table FixFlo.Contractor 
|Idx |Name |Data Type |
|---|---|---|
| &#128270; | Address\_AddressLine1| varchar(8000)  |
| &#128270; | Address\_AddressLine2| varchar(8000)  |
| &#128270; | Address\_Country| varchar(8000)  |
| &#128270; | Address\_County| varchar(8000)  |
| &#128270; | Address\_PostCode| varchar(8000)  |
| &#128270; | Address\_Town| varchar(8000)  |
| &#128270; | Brand| varchar(8000)  |
| &#128270; | Certifications| varchar(8000)  |
| &#128270; | CompanyName| varchar(8000)  |
| &#128270; | ContactNumber| varchar(8000)  |
| &#128270; | ContactNumberAlt| varchar(8000)  |
| &#128270; | DisplayName| varchar(8000)  |
| &#128270; | EmailAddress| varchar(8000)  |
| &#128270; | EmailCC| varchar(8000)  |
| &#128270; | ExternalRef| varchar(8000)  |
| &#128270; | FirstName| varchar(8000)  |
| &#128270; | Id| varchar(8000)  |
| &#128270; | IngestedUTC| varchar(8000)  |
| &#128270; | InvoiceSettings\_BankAccountNumber| varchar(8000)  |
| &#128270; | InvoiceSettings\_BankAccountSortCode| varchar(8000)  |
| &#128270; | InvoiceSettings\_CompanyNumber| varchar(8000)  |
| &#128270; | InvoiceSettings\_DefaultDueDateInterval| bigint  |
| &#128270; | InvoiceSettings\_DefaultTaxRate| float(53)  |
| &#128270; | InvoiceSettings\_InvoiceAddress\_AddressLine1| varchar(8000)  |
| &#128270; | InvoiceSettings\_InvoiceAddress\_AddressLine2| varchar(8000)  |
| &#128270; | InvoiceSettings\_InvoiceAddress\_Country| varchar(8000)  |
| &#128270; | InvoiceSettings\_InvoiceAddress\_County| varchar(8000)  |
| &#128270; | InvoiceSettings\_InvoiceAddress\_PostCode| varchar(8000)  |
| &#128270; | InvoiceSettings\_InvoiceAddress\_Town| varchar(8000)  |
| &#128270; | InvoiceSettings\_TermsOfPayment| varchar(8000)  |
| &#128270; | InvoiceSettings\_VatNumber| varchar(8000)  |
| &#128270; | IsDeleted| bit  |
| &#128270; | Services| varchar(8000)  |
| &#128270; | Surname| varchar(8000)  |
| &#128270; | Title| varchar(8000)  |
| &#128270; | UpdateDate| varchar(8000)  |
| &#128270; | \_source\_page| bigint  |
| &#128270; | \_meta\_source\_file\_name| varchar(8000)  |
| &#128270; | \_meta\_source\_file\_path| varchar(8000)  |
| &#128270; | \_meta\_raw\_row\_number| int  |
| &#128270; | \_meta\_row\_hash| varchar(8000)  |
| &#128270; | \_meta\_pipeline\_id| varchar(8000)  |
| &#128270; | \_meta\_ingest\_ts| datetime2(26)  |


##### Indexes 
|Type |Name |On |
|---|---|---|
| &#128270;  | ClusteredIndex | ON Address\_AddressLine1|
| &#128270;  | ClusteredIndex | ON Address\_AddressLine2|
| &#128270;  | ClusteredIndex | ON Address\_Country|
| &#128270;  | ClusteredIndex | ON Address\_County|
| &#128270;  | ClusteredIndex | ON Address\_PostCode|
| &#128270;  | ClusteredIndex | ON Address\_Town|
| &#128270;  | ClusteredIndex | ON Brand|
| &#128270;  | ClusteredIndex | ON Certifications|
| &#128270;  | ClusteredIndex | ON CompanyName|
| &#128270;  | ClusteredIndex | ON ContactNumber|
| &#128270;  | ClusteredIndex | ON ContactNumberAlt|
| &#128270;  | ClusteredIndex | ON DisplayName|
| &#128270;  | ClusteredIndex | ON EmailAddress|
| &#128270;  | ClusteredIndex | ON EmailCC|
| &#128270;  | ClusteredIndex | ON ExternalRef|
| &#128270;  | ClusteredIndex | ON FirstName|
| &#128270;  | ClusteredIndex | ON Id|
| &#128270;  | ClusteredIndex | ON IngestedUTC|
| &#128270;  | ClusteredIndex | ON InvoiceSettings\_BankAccountNumber|
| &#128270;  | ClusteredIndex | ON InvoiceSettings\_BankAccountSortCode|
| &#128270;  | ClusteredIndex | ON InvoiceSettings\_CompanyNumber|
| &#128270;  | ClusteredIndex | ON InvoiceSettings\_DefaultDueDateInterval|
| &#128270;  | ClusteredIndex | ON InvoiceSettings\_DefaultTaxRate|
| &#128270;  | ClusteredIndex | ON InvoiceSettings\_InvoiceAddress\_AddressLine1|
| &#128270;  | ClusteredIndex | ON InvoiceSettings\_InvoiceAddress\_AddressLine2|
| &#128270;  | ClusteredIndex | ON InvoiceSettings\_InvoiceAddress\_Country|
| &#128270;  | ClusteredIndex | ON InvoiceSettings\_InvoiceAddress\_County|
| &#128270;  | ClusteredIndex | ON InvoiceSettings\_InvoiceAddress\_PostCode|
| &#128270;  | ClusteredIndex | ON InvoiceSettings\_InvoiceAddress\_Town|
| &#128270;  | ClusteredIndex | ON InvoiceSettings\_TermsOfPayment|
| &#128270;  | ClusteredIndex | ON InvoiceSettings\_VatNumber|
| &#128270;  | ClusteredIndex | ON IsDeleted|
| &#128270;  | ClusteredIndex | ON Services|
| &#128270;  | ClusteredIndex | ON Surname|
| &#128270;  | ClusteredIndex | ON Title|
| &#128270;  | ClusteredIndex | ON UpdateDate|
| &#128270;  | ClusteredIndex | ON \_source\_page|
| &#128270;  | ClusteredIndex | ON \_meta\_source\_file\_name|
| &#128270;  | ClusteredIndex | ON \_meta\_source\_file\_path|
| &#128270;  | ClusteredIndex | ON \_meta\_raw\_row\_number|
| &#128270;  | ClusteredIndex | ON \_meta\_row\_hash|
| &#128270;  | ClusteredIndex | ON \_meta\_pipeline\_id|
| &#128270;  | ClusteredIndex | ON \_meta\_ingest\_ts|



### Table FixFlo.Estate 
|Idx |Name |Data Type |
|---|---|---|
| &#128270; | AssignedAgent\_Brand| varchar(8000)  |
| &#128270; | AssignedAgent\_ContactNo| varchar(8000)  |
| &#128270; | AssignedAgent\_DisplayName| varchar(8000)  |
| &#128270; | AssignedAgent\_EmailAddress| varchar(8000)  |
| &#128270; | AssignedAgent\_EmailCC| varchar(8000)  |
| &#128270; | AssignedAgent\_ExternalRef| varchar(8000)  |
| &#128270; | AssignedAgent\_Id| varchar(8000)  |
| &#128270; | AssignedAgent\_IsDeleted| bit  |
| &#128270; | AssignedAgent\_UpdateDate| varchar(8000)  |
| &#128270; | ExternalEstateRef| varchar(8000)  |
| &#128270; | Id| bigint  |
| &#128270; | IngestedUTC| varchar(8000)  |
| &#128270; | IsDeleted| bit  |
| &#128270; | Name| varchar(8000)  |
| &#128270; | UpdateDate| varchar(8000)  |
| &#128270; | \_source\_page| bigint  |
| &#128270; | \_meta\_source\_file\_name| varchar(8000)  |
| &#128270; | \_meta\_source\_file\_path| varchar(8000)  |
| &#128270; | \_meta\_raw\_row\_number| int  |
| &#128270; | \_meta\_row\_hash| varchar(8000)  |
| &#128270; | \_meta\_pipeline\_id| varchar(8000)  |
| &#128270; | \_meta\_ingest\_ts| datetime2(26)  |


##### Indexes 
|Type |Name |On |
|---|---|---|
| &#128270;  | ClusteredIndex | ON AssignedAgent\_Brand|
| &#128270;  | ClusteredIndex | ON AssignedAgent\_ContactNo|
| &#128270;  | ClusteredIndex | ON AssignedAgent\_DisplayName|
| &#128270;  | ClusteredIndex | ON AssignedAgent\_EmailAddress|
| &#128270;  | ClusteredIndex | ON AssignedAgent\_EmailCC|
| &#128270;  | ClusteredIndex | ON AssignedAgent\_ExternalRef|
| &#128270;  | ClusteredIndex | ON AssignedAgent\_Id|
| &#128270;  | ClusteredIndex | ON AssignedAgent\_IsDeleted|
| &#128270;  | ClusteredIndex | ON AssignedAgent\_UpdateDate|
| &#128270;  | ClusteredIndex | ON ExternalEstateRef|
| &#128270;  | ClusteredIndex | ON Id|
| &#128270;  | ClusteredIndex | ON IngestedUTC|
| &#128270;  | ClusteredIndex | ON IsDeleted|
| &#128270;  | ClusteredIndex | ON Name|
| &#128270;  | ClusteredIndex | ON UpdateDate|
| &#128270;  | ClusteredIndex | ON \_source\_page|
| &#128270;  | ClusteredIndex | ON \_meta\_source\_file\_name|
| &#128270;  | ClusteredIndex | ON \_meta\_source\_file\_path|
| &#128270;  | ClusteredIndex | ON \_meta\_raw\_row\_number|
| &#128270;  | ClusteredIndex | ON \_meta\_row\_hash|
| &#128270;  | ClusteredIndex | ON \_meta\_pipeline\_id|
| &#128270;  | ClusteredIndex | ON \_meta\_ingest\_ts|



### Table FixFlo.Issue 
|Idx |Name |Data Type |
|---|---|---|
| &#128270; | AdditionalDetails| varchar(8000)  |
| &#128270; | Address\_AddressLine1| varchar(8000)  |
| &#128270; | Address\_AddressLine2| varchar(8000)  |
| &#128270; | Address\_Country| varchar(8000)  |
| &#128270; | Address\_County| varchar(8000)  |
| &#128270; | Address\_PostCode| varchar(8000)  |
| &#128270; | Address\_Town| varchar(8000)  |
| &#128270; | AgencyId| varchar(8000)  |
| &#128270; | AgencyName| varchar(8000)  |
| &#128270; | AssignedAgent\_Brand| varchar(8000)  |
| &#128270; | AssignedAgent\_ContactNo| varchar(8000)  |
| &#128270; | AssignedAgent\_DisplayName| varchar(8000)  |
| &#128270; | AssignedAgent\_EmailAddress| varchar(8000)  |
| &#128270; | AssignedAgent\_EmailCC| varchar(8000)  |
| &#128270; | AssignedAgent\_ExternalRef| varchar(8000)  |
| &#128270; | AssignedAgent\_Id| varchar(8000)  |
| &#128270; | AssignedAgent\_IsDeleted| bit  |
| &#128270; | AssignedAgent\_UpdateDate| varchar(8000)  |
| &#128270; | AttendenceDate| varchar(8000)  |
| &#128270; | Block\_Address\_AddressLine1| varchar(8000)  |
| &#128270; | Block\_Address\_AddressLine2| varchar(8000)  |
| &#128270; | Block\_Address\_Country| varchar(8000)  |
| &#128270; | Block\_Address\_County| varchar(8000)  |
| &#128270; | Block\_Address\_PostCode| varchar(8000)  |
| &#128270; | Block\_Address\_Town| varchar(8000)  |
| &#128270; | Block\_AssignedAgent\_Brand| varchar(8000)  |
| &#128270; | Block\_AssignedAgent\_ContactNo| varchar(8000)  |
| &#128270; | Block\_AssignedAgent\_DisplayName| varchar(8000)  |
| &#128270; | Block\_AssignedAgent\_EmailAddress| varchar(8000)  |
| &#128270; | Block\_AssignedAgent\_EmailCC| varchar(8000)  |
| &#128270; | Block\_AssignedAgent\_ExternalRef| varchar(8000)  |
| &#128270; | Block\_AssignedAgent\_Id| varchar(8000)  |
| &#128270; | Block\_AssignedAgent\_IsDeleted| bit  |
| &#128270; | Block\_AssignedAgent\_UpdateDate| varchar(8000)  |
| &#128270; | Block\_Brand| varchar(8000)  |
| &#128270; | Block\_Created| varchar(8000)  |
| &#128270; | Block\_EstateId| bigint  |
| &#128270; | Block\_ExternalBlockReference| varchar(8000)  |
| &#128270; | Block\_ExternalEstateRef| varchar(8000)  |
| &#128270; | Block\_ExternalLandlordRef| varchar(8000)  |
| &#128270; | Block\_Id| bigint  |
| &#128270; | Block\_IsDeleted| bit  |
| &#128270; | Block\_IsStandAlone| bit  |
| &#128270; | Block\_KeyReference| varchar(8000)  |
| &#128270; | Block\_LandlordId| varchar(8000)  |
| &#128270; | Block\_ManagementEndDate| varchar(8000)  |
| &#128270; | Block\_ManagementStartDate| varchar(8000)  |
| &#128270; | Block\_Name| varchar(8000)  |
| &#128270; | Block\_PropertyManager\_Brand| varchar(8000)  |
| &#128270; | Block\_PropertyManager\_ContactNo| varchar(8000)  |
| &#128270; | Block\_PropertyManager\_DisplayName| varchar(8000)  |
| &#128270; | Block\_PropertyManager\_EmailAddress| varchar(8000)  |
| &#128270; | Block\_PropertyManager\_EmailCC| varchar(8000)  |
| &#128270; | Block\_PropertyManager\_ExternalRef| varchar(8000)  |
| &#128270; | Block\_PropertyManager\_Id| varchar(8000)  |
| &#128270; | Block\_PropertyManager\_IsDeleted| bit  |
| &#128270; | Block\_PropertyManager\_UpdateDate| varchar(8000)  |
| &#128270; | Block\_UpdateDate| varchar(8000)  |
| &#128270; | Block\_Warranties| varchar(8000)  |
| &#128270; | BlockName| varchar(8000)  |
| &#128270; | CallbackId| varchar(8000)  |
| &#128270; | CloseReason| varchar(8000)  |
| &#128270; | CloseReasonDescription| varchar(8000)  |
| &#128270; | ContactNumber| varchar(8000)  |
| &#128270; | ContactNumberAlt| varchar(8000)  |
| &#128270; | CostCode| varchar(8000)  |
| &#128270; | Created| varchar(8000)  |
| &#128270; | EmailAddress| varchar(8000)  |
| &#128270; | ExternalRef| varchar(8000)  |
| &#128270; | ExternalRefTenancyAgreement| varchar(8000)  |
| &#128270; | ExternalRefTenant| varchar(8000)  |
| &#128270; | FaultCategory| varchar(8000)  |
| &#128270; | FaultNotes| varchar(8000)  |
| &#128270; | FaultPriority| bigint  |
| &#128270; | FaultTitle| varchar(8000)  |
| &#128270; | FaultTree\_FaultId| bigint  |
| &#128270; | FaultTree\_FaultTreeParent0| bigint  |
| &#128270; | FaultTree\_FaultTreeParent1| bigint  |
| &#128270; | FaultTree\_FaultTreeParent2| bigint  |
| &#128270; | Firstname| varchar(8000)  |
| &#128270; | Id| varchar(8000)  |
| &#128270; | InactiveJobs| varchar(8000)  |
| &#128270; | InvoiceRecipient| varchar(8000)  |
| &#128270; | IsCommunal| bit  |
| &#128270; | IsEmergency| varchar(8000)  |
| &#128270; | IsPlannedMaintenance| bit  |
| &#128270; | IssueType| varchar(8000)  |
| &#128270; | Job\_AppointmentDescription| varchar(8000)  |
| &#128270; | Job\_AppointmentRange| varchar(8000)  |
| &#128270; | Job\_Appointments| varchar(8000)  |
| &#128270; | Job\_Contractor\_Address\_AddressLine1| varchar(8000)  |
| &#128270; | Job\_Contractor\_Address\_AddressLine2| varchar(8000)  |
| &#128270; | Job\_Contractor\_Address\_Country| varchar(8000)  |
| &#128270; | Job\_Contractor\_Address\_County| varchar(8000)  |
| &#128270; | Job\_Contractor\_Address\_PostCode| varchar(8000)  |
| &#128270; | Job\_Contractor\_Address\_Town| varchar(8000)  |
| &#128270; | Job\_Contractor\_Brand| varchar(8000)  |
| &#128270; | Job\_Contractor\_Certifications| varchar(8000)  |
| &#128270; | Job\_Contractor\_CompanyName| varchar(8000)  |
| &#128270; | Job\_Contractor\_ContactNumber| varchar(8000)  |
| &#128270; | Job\_Contractor\_ContactNumberAlt| varchar(8000)  |
| &#128270; | Job\_Contractor\_DisplayName| varchar(8000)  |
| &#128270; | Job\_Contractor\_EmailAddress| varchar(8000)  |
| &#128270; | Job\_Contractor\_EmailCC| varchar(8000)  |
| &#128270; | Job\_Contractor\_ExternalRef| varchar(8000)  |
| &#128270; | Job\_Contractor\_FirstName| varchar(8000)  |
| &#128270; | Job\_Contractor\_Id| varchar(8000)  |
| &#128270; | Job\_Contractor\_InvoiceSettings\_BankAccountNumber| varchar(8000)  |
| &#128270; | Job\_Contractor\_InvoiceSettings\_BankAccountSortCode| varchar(8000)  |
| &#128270; | Job\_Contractor\_InvoiceSettings\_CompanyNumber| varchar(8000)  |
| &#128270; | Job\_Contractor\_InvoiceSettings\_DefaultDueDateInterval| bigint  |
| &#128270; | Job\_Contractor\_InvoiceSettings\_DefaultTaxRate| float(53)  |
| &#128270; | Job\_Contractor\_InvoiceSettings\_InvoiceAddress\_AddressLine1| varchar(8000)  |
| &#128270; | Job\_Contractor\_InvoiceSettings\_InvoiceAddress\_AddressLine2| varchar(8000)  |
| &#128270; | Job\_Contractor\_InvoiceSettings\_InvoiceAddress\_Country| varchar(8000)  |
| &#128270; | Job\_Contractor\_InvoiceSettings\_InvoiceAddress\_County| varchar(8000)  |
| &#128270; | Job\_Contractor\_InvoiceSettings\_InvoiceAddress\_PostCode| varchar(8000)  |
| &#128270; | Job\_Contractor\_InvoiceSettings\_InvoiceAddress\_Town| varchar(8000)  |
| &#128270; | Job\_Contractor\_InvoiceSettings\_TermsOfPayment| varchar(8000)  |
| &#128270; | Job\_Contractor\_InvoiceSettings\_VatNumber| varchar(8000)  |
| &#128270; | Job\_Contractor\_IsDeleted| bit  |
| &#128270; | Job\_Contractor\_Services| varchar(8000)  |
| &#128270; | Job\_Contractor\_Surname| varchar(8000)  |
| &#128270; | Job\_Contractor\_Title| varchar(8000)  |
| &#128270; | Job\_Contractor\_UpdateDate| varchar(8000)  |
| &#128270; | Job\_ContractorNetwork| varchar(8000)  |
| &#128270; | Job\_ContractorNetworkJobRef| varchar(8000)  |
| &#128270; | Job\_CreatedDate| varchar(8000)  |
| &#128270; | Job\_ExternalRefJob| varchar(8000)  |
| &#128270; | Job\_ExternalUserApproval| varchar(8000)  |
| &#128270; | Job\_Id| varchar(8000)  |
| &#128270; | Job\_InvoiceComments| varchar(8000)  |
| &#128270; | Job\_InvoiceDate| varchar(8000)  |
| &#128270; | Job\_InvoiceDueDate| varchar(8000)  |
| &#128270; | Job\_IsActive| bit  |
| &#128270; | Job\_IssueNo| varchar(8000)  |
| &#128270; | Job\_JobCompleted| varchar(8000)  |
| &#128270; | Job\_JobDuration| varchar(8000)  |
| &#128270; | Job\_JobInvoiceMethod| varchar(8000)  |
| &#128270; | Job\_JobInvoiceNumber| varchar(8000)  |
| &#128270; | Job\_JobberAgreedWithTenantStartDate| bit  |
| &#128270; | Job\_JobberNotes| varchar(8000)  |
| &#128270; | Job\_Landlord| varchar(8000)  |
| &#128270; | Job\_LandlordApproval| varchar(8000)  |
| &#128270; | Job\_PriceAgencyPayableGross| float(53)  |
| &#128270; | Job\_PriceAgencyPayableNet| float(53)  |
| &#128270; | Job\_PriceAgencyPayableTax| float(53)  |
| &#128270; | Job\_PriceAgencyReceivableGross| float(53)  |
| &#128270; | Job\_PriceAgencyReceivableNet| float(53)  |
| &#128270; | Job\_PriceAgencyReceivableTax| float(53)  |
| &#128270; | Job\_QuotedPriceAgencyPayableGross| bigint  |
| &#128270; | Job\_QuotedPriceAgencyPayableNet| bigint  |
| &#128270; | Job\_QuotedPriceAgencyPayableTax| bigint  |
| &#128270; | Job\_QuotedPriceAgencyReceivableGross| bigint  |
| &#128270; | Job\_QuotedPriceAgencyReceivableNet| bigint  |
| &#128270; | Job\_QuotedPriceAgencyReceivableTax| bigint  |
| &#128270; | Job\_StartDate| varchar(8000)  |
| &#128270; | Job\_TenantAcceptedStartDate| varchar(8000)  |
| &#128270; | Job\_TenantNotes| varchar(8000)  |
| &#128270; | Job\_UpdateDate| varchar(8000)  |
| &#128270; | Job\_WorksExpiryDate| varchar(8000)  |
| &#128270; | Landlord\_Address\_AddressLine1| varchar(8000)  |
| &#128270; | Landlord\_Address\_AddressLine2| varchar(8000)  |
| &#128270; | Landlord\_Address\_Country| varchar(8000)  |
| &#128270; | Landlord\_Address\_County| varchar(8000)  |
| &#128270; | Landlord\_Address\_PostCode| varchar(8000)  |
| &#128270; | Landlord\_Address\_Town| varchar(8000)  |
| &#128270; | Landlord\_AssignedAgent| varchar(8000)  |
| &#128270; | Landlord\_Brand| varchar(8000)  |
| &#128270; | Landlord\_CompanyName| varchar(8000)  |
| &#128270; | Landlord\_ContactNumber| varchar(8000)  |
| &#128270; | Landlord\_ContactNumberAlt| varchar(8000)  |
| &#128270; | Landlord\_DisplayName| varchar(8000)  |
| &#128270; | Landlord\_EmailAddress| varchar(8000)  |
| &#128270; | Landlord\_EmailCC| varchar(8000)  |
| &#128270; | Landlord\_ExternalRef| varchar(8000)  |
| &#128270; | Landlord\_FirstName| varchar(8000)  |
| &#128270; | Landlord\_Id| varchar(8000)  |
| &#128270; | Landlord\_IsDeleted| bit  |
| &#128270; | Landlord\_Surname| varchar(8000)  |
| &#128270; | Landlord\_Title| varchar(8000)  |
| &#128270; | Landlord\_UpdateDate| varchar(8000)  |
| &#128270; | Landlord\_WorksAuthorisationLimit| varchar(8000)  |
| &#128270; | Media| varchar(8000)  |
| &#128270; | Property\_Address\_AddressLine1| varchar(8000)  |
| &#128270; | Property\_Address\_AddressLine2| varchar(8000)  |
| &#128270; | Property\_Address\_Country| varchar(8000)  |
| &#128270; | Property\_Address\_County| varchar(8000)  |
| &#128270; | Property\_Address\_PostCode| varchar(8000)  |
| &#128270; | Property\_Address\_Town| varchar(8000)  |
| &#128270; | Property\_ArchiveStatus| varchar(8000)  |
| &#128270; | Property\_AssignedAgent| varchar(8000)  |
| &#128270; | Property\_AssignedTeam| varchar(8000)  |
| &#128270; | Property\_BlockId| bigint  |
| &#128270; | Property\_Brand| varchar(8000)  |
| &#128270; | Property\_Created| varchar(8000)  |
| &#128270; | Property\_ExternalPropertyRef| varchar(8000)  |
| &#128270; | Property\_Id| bigint  |
| &#128270; | Property\_IsDeleted| bit  |
| &#128270; | Property\_IsNotManaged| bit  |
| &#128270; | Property\_KeyReference| varchar(8000)  |
| &#128270; | Property\_PropertyAddressId| bigint  |
| &#128270; | Property\_PropertyManager| varchar(8000)  |
| &#128270; | Property\_UpdateDate| varchar(8000)  |
| &#128270; | Property\_Warranties| varchar(8000)  |
| &#128270; | PropertyAddressId| bigint  |
| &#128270; | QuoteEndTime| varchar(8000)  |
| &#128270; | QuoteNotes| varchar(8000)  |
| &#128270; | QuoteRequests| varchar(8000)  |
| &#128270; | Quotes| varchar(8000)  |
| &#128270; | RaisedByAgent\_Brand| varchar(8000)  |
| &#128270; | RaisedByAgent\_ContactNo| varchar(8000)  |
| &#128270; | RaisedByAgent\_DisplayName| varchar(8000)  |
| &#128270; | RaisedByAgent\_EmailAddress| varchar(8000)  |
| &#128270; | RaisedByAgent\_EmailCC| varchar(8000)  |
| &#128270; | RaisedByAgent\_ExternalRef| varchar(8000)  |
| &#128270; | RaisedByAgent\_Id| varchar(8000)  |
| &#128270; | RaisedByAgent\_IsDeleted| bit  |
| &#128270; | RaisedByAgent\_UpdateDate| varchar(8000)  |
| &#128270; | Reporter\_Id| varchar(8000)  |
| &#128270; | Reporter\_Role| varchar(8000)  |
| &#128270; | Salutation| varchar(8000)  |
| &#128270; | ServiceEventId| varchar(8000)  |
| &#128270; | Status| varchar(8000)  |
| &#128270; | StatusChanged| varchar(8000)  |
| &#128270; | Surname| varchar(8000)  |
| &#128270; | TenantAcceptComplete| varchar(8000)  |
| &#128270; | TenantId| varchar(8000)  |
| &#128270; | TenantNotes| varchar(8000)  |
| &#128270; | TenantPresenceRequested| bit  |
| &#128270; | TermsAccepted| bit  |
| &#128270; | Title| varchar(8000)  |
| &#128270; | VulnerableOccupiers| bit  |
| &#128270; | WorksAuthorisationLimit| float(53)  |
| &#128270; | WorksPaidBy| varchar(8000)  |
| &#128270; | \_meta\_source\_file\_name| varchar(8000)  |
| &#128270; | \_meta\_source\_file\_path| varchar(8000)  |
| &#128270; | \_meta\_raw\_row\_number| int  |
| &#128270; | \_meta\_row\_hash| varchar(8000)  |
| &#128270; | \_meta\_pipeline\_id| varchar(8000)  |
| &#128270; | \_meta\_ingest\_ts| datetime2(26)  |


##### Indexes 
|Type |Name |On |
|---|---|---|
| &#128270;  | ClusteredIndex | ON AdditionalDetails|
| &#128270;  | ClusteredIndex | ON Address\_AddressLine1|
| &#128270;  | ClusteredIndex | ON Address\_AddressLine2|
| &#128270;  | ClusteredIndex | ON Address\_Country|
| &#128270;  | ClusteredIndex | ON Address\_County|
| &#128270;  | ClusteredIndex | ON Address\_PostCode|
| &#128270;  | ClusteredIndex | ON Address\_Town|
| &#128270;  | ClusteredIndex | ON AgencyId|
| &#128270;  | ClusteredIndex | ON AgencyName|
| &#128270;  | ClusteredIndex | ON AssignedAgent\_Brand|
| &#128270;  | ClusteredIndex | ON AssignedAgent\_ContactNo|
| &#128270;  | ClusteredIndex | ON AssignedAgent\_DisplayName|
| &#128270;  | ClusteredIndex | ON AssignedAgent\_EmailAddress|
| &#128270;  | ClusteredIndex | ON AssignedAgent\_EmailCC|
| &#128270;  | ClusteredIndex | ON AssignedAgent\_ExternalRef|
| &#128270;  | ClusteredIndex | ON AssignedAgent\_Id|
| &#128270;  | ClusteredIndex | ON AssignedAgent\_IsDeleted|
| &#128270;  | ClusteredIndex | ON AssignedAgent\_UpdateDate|
| &#128270;  | ClusteredIndex | ON AttendenceDate|
| &#128270;  | ClusteredIndex | ON Block\_Address\_AddressLine1|
| &#128270;  | ClusteredIndex | ON Block\_Address\_AddressLine2|
| &#128270;  | ClusteredIndex | ON Block\_Address\_Country|
| &#128270;  | ClusteredIndex | ON Block\_Address\_County|
| &#128270;  | ClusteredIndex | ON Block\_Address\_PostCode|
| &#128270;  | ClusteredIndex | ON Block\_Address\_Town|
| &#128270;  | ClusteredIndex | ON Block\_AssignedAgent\_Brand|
| &#128270;  | ClusteredIndex | ON Block\_AssignedAgent\_ContactNo|
| &#128270;  | ClusteredIndex | ON Block\_AssignedAgent\_DisplayName|
| &#128270;  | ClusteredIndex | ON Block\_AssignedAgent\_EmailAddress|
| &#128270;  | ClusteredIndex | ON Block\_AssignedAgent\_EmailCC|
| &#128270;  | ClusteredIndex | ON Block\_AssignedAgent\_ExternalRef|
| &#128270;  | ClusteredIndex | ON Block\_AssignedAgent\_Id|
| &#128270;  | ClusteredIndex | ON Block\_AssignedAgent\_IsDeleted|
| &#128270;  | ClusteredIndex | ON Block\_AssignedAgent\_UpdateDate|
| &#128270;  | ClusteredIndex | ON Block\_Brand|
| &#128270;  | ClusteredIndex | ON Block\_Created|
| &#128270;  | ClusteredIndex | ON Block\_EstateId|
| &#128270;  | ClusteredIndex | ON Block\_ExternalBlockReference|
| &#128270;  | ClusteredIndex | ON Block\_ExternalEstateRef|
| &#128270;  | ClusteredIndex | ON Block\_ExternalLandlordRef|
| &#128270;  | ClusteredIndex | ON Block\_Id|
| &#128270;  | ClusteredIndex | ON Block\_IsDeleted|
| &#128270;  | ClusteredIndex | ON Block\_IsStandAlone|
| &#128270;  | ClusteredIndex | ON Block\_KeyReference|
| &#128270;  | ClusteredIndex | ON Block\_LandlordId|
| &#128270;  | ClusteredIndex | ON Block\_ManagementEndDate|
| &#128270;  | ClusteredIndex | ON Block\_ManagementStartDate|
| &#128270;  | ClusteredIndex | ON Block\_Name|
| &#128270;  | ClusteredIndex | ON Block\_PropertyManager\_Brand|
| &#128270;  | ClusteredIndex | ON Block\_PropertyManager\_ContactNo|
| &#128270;  | ClusteredIndex | ON Block\_PropertyManager\_DisplayName|
| &#128270;  | ClusteredIndex | ON Block\_PropertyManager\_EmailAddress|
| &#128270;  | ClusteredIndex | ON Block\_PropertyManager\_EmailCC|
| &#128270;  | ClusteredIndex | ON Block\_PropertyManager\_ExternalRef|
| &#128270;  | ClusteredIndex | ON Block\_PropertyManager\_Id|
| &#128270;  | ClusteredIndex | ON Block\_PropertyManager\_IsDeleted|
| &#128270;  | ClusteredIndex | ON Block\_PropertyManager\_UpdateDate|
| &#128270;  | ClusteredIndex | ON Block\_UpdateDate|
| &#128270;  | ClusteredIndex | ON Block\_Warranties|
| &#128270;  | ClusteredIndex | ON BlockName|
| &#128270;  | ClusteredIndex | ON CallbackId|
| &#128270;  | ClusteredIndex | ON CloseReason|
| &#128270;  | ClusteredIndex | ON CloseReasonDescription|
| &#128270;  | ClusteredIndex | ON ContactNumber|
| &#128270;  | ClusteredIndex | ON ContactNumberAlt|
| &#128270;  | ClusteredIndex | ON CostCode|
| &#128270;  | ClusteredIndex | ON Created|
| &#128270;  | ClusteredIndex | ON EmailAddress|
| &#128270;  | ClusteredIndex | ON ExternalRef|
| &#128270;  | ClusteredIndex | ON ExternalRefTenancyAgreement|
| &#128270;  | ClusteredIndex | ON ExternalRefTenant|
| &#128270;  | ClusteredIndex | ON FaultCategory|
| &#128270;  | ClusteredIndex | ON FaultNotes|
| &#128270;  | ClusteredIndex | ON FaultPriority|
| &#128270;  | ClusteredIndex | ON FaultTitle|
| &#128270;  | ClusteredIndex | ON FaultTree\_FaultId|
| &#128270;  | ClusteredIndex | ON FaultTree\_FaultTreeParent0|
| &#128270;  | ClusteredIndex | ON FaultTree\_FaultTreeParent1|
| &#128270;  | ClusteredIndex | ON FaultTree\_FaultTreeParent2|
| &#128270;  | ClusteredIndex | ON Firstname|
| &#128270;  | ClusteredIndex | ON Id|
| &#128270;  | ClusteredIndex | ON InactiveJobs|
| &#128270;  | ClusteredIndex | ON InvoiceRecipient|
| &#128270;  | ClusteredIndex | ON IsCommunal|
| &#128270;  | ClusteredIndex | ON IsEmergency|
| &#128270;  | ClusteredIndex | ON IsPlannedMaintenance|
| &#128270;  | ClusteredIndex | ON IssueType|
| &#128270;  | ClusteredIndex | ON Job\_AppointmentDescription|
| &#128270;  | ClusteredIndex | ON Job\_AppointmentRange|
| &#128270;  | ClusteredIndex | ON Job\_Appointments|
| &#128270;  | ClusteredIndex | ON Job\_Contractor\_Address\_AddressLine1|
| &#128270;  | ClusteredIndex | ON Job\_Contractor\_Address\_AddressLine2|
| &#128270;  | ClusteredIndex | ON Job\_Contractor\_Address\_Country|
| &#128270;  | ClusteredIndex | ON Job\_Contractor\_Address\_County|
| &#128270;  | ClusteredIndex | ON Job\_Contractor\_Address\_PostCode|
| &#128270;  | ClusteredIndex | ON Job\_Contractor\_Address\_Town|
| &#128270;  | ClusteredIndex | ON Job\_Contractor\_Brand|
| &#128270;  | ClusteredIndex | ON Job\_Contractor\_Certifications|
| &#128270;  | ClusteredIndex | ON Job\_Contractor\_CompanyName|
| &#128270;  | ClusteredIndex | ON Job\_Contractor\_ContactNumber|
| &#128270;  | ClusteredIndex | ON Job\_Contractor\_ContactNumberAlt|
| &#128270;  | ClusteredIndex | ON Job\_Contractor\_DisplayName|
| &#128270;  | ClusteredIndex | ON Job\_Contractor\_EmailAddress|
| &#128270;  | ClusteredIndex | ON Job\_Contractor\_EmailCC|
| &#128270;  | ClusteredIndex | ON Job\_Contractor\_ExternalRef|
| &#128270;  | ClusteredIndex | ON Job\_Contractor\_FirstName|
| &#128270;  | ClusteredIndex | ON Job\_Contractor\_Id|
| &#128270;  | ClusteredIndex | ON Job\_Contractor\_InvoiceSettings\_BankAccountNumber|
| &#128270;  | ClusteredIndex | ON Job\_Contractor\_InvoiceSettings\_BankAccountSortCode|
| &#128270;  | ClusteredIndex | ON Job\_Contractor\_InvoiceSettings\_CompanyNumber|
| &#128270;  | ClusteredIndex | ON Job\_Contractor\_InvoiceSettings\_DefaultDueDateInterval|
| &#128270;  | ClusteredIndex | ON Job\_Contractor\_InvoiceSettings\_DefaultTaxRate|
| &#128270;  | ClusteredIndex | ON Job\_Contractor\_InvoiceSettings\_InvoiceAddress\_AddressLine1|
| &#128270;  | ClusteredIndex | ON Job\_Contractor\_InvoiceSettings\_InvoiceAddress\_AddressLine2|
| &#128270;  | ClusteredIndex | ON Job\_Contractor\_InvoiceSettings\_InvoiceAddress\_Country|
| &#128270;  | ClusteredIndex | ON Job\_Contractor\_InvoiceSettings\_InvoiceAddress\_County|
| &#128270;  | ClusteredIndex | ON Job\_Contractor\_InvoiceSettings\_InvoiceAddress\_PostCode|
| &#128270;  | ClusteredIndex | ON Job\_Contractor\_InvoiceSettings\_InvoiceAddress\_Town|
| &#128270;  | ClusteredIndex | ON Job\_Contractor\_InvoiceSettings\_TermsOfPayment|
| &#128270;  | ClusteredIndex | ON Job\_Contractor\_InvoiceSettings\_VatNumber|
| &#128270;  | ClusteredIndex | ON Job\_Contractor\_IsDeleted|
| &#128270;  | ClusteredIndex | ON Job\_Contractor\_Services|
| &#128270;  | ClusteredIndex | ON Job\_Contractor\_Surname|
| &#128270;  | ClusteredIndex | ON Job\_Contractor\_Title|
| &#128270;  | ClusteredIndex | ON Job\_Contractor\_UpdateDate|
| &#128270;  | ClusteredIndex | ON Job\_ContractorNetwork|
| &#128270;  | ClusteredIndex | ON Job\_ContractorNetworkJobRef|
| &#128270;  | ClusteredIndex | ON Job\_CreatedDate|
| &#128270;  | ClusteredIndex | ON Job\_ExternalRefJob|
| &#128270;  | ClusteredIndex | ON Job\_ExternalUserApproval|
| &#128270;  | ClusteredIndex | ON Job\_Id|
| &#128270;  | ClusteredIndex | ON Job\_InvoiceComments|
| &#128270;  | ClusteredIndex | ON Job\_InvoiceDate|
| &#128270;  | ClusteredIndex | ON Job\_InvoiceDueDate|
| &#128270;  | ClusteredIndex | ON Job\_IsActive|
| &#128270;  | ClusteredIndex | ON Job\_IssueNo|
| &#128270;  | ClusteredIndex | ON Job\_JobCompleted|
| &#128270;  | ClusteredIndex | ON Job\_JobDuration|
| &#128270;  | ClusteredIndex | ON Job\_JobInvoiceMethod|
| &#128270;  | ClusteredIndex | ON Job\_JobInvoiceNumber|
| &#128270;  | ClusteredIndex | ON Job\_JobberAgreedWithTenantStartDate|
| &#128270;  | ClusteredIndex | ON Job\_JobberNotes|
| &#128270;  | ClusteredIndex | ON Job\_Landlord|
| &#128270;  | ClusteredIndex | ON Job\_LandlordApproval|
| &#128270;  | ClusteredIndex | ON Job\_PriceAgencyPayableGross|
| &#128270;  | ClusteredIndex | ON Job\_PriceAgencyPayableNet|
| &#128270;  | ClusteredIndex | ON Job\_PriceAgencyPayableTax|
| &#128270;  | ClusteredIndex | ON Job\_PriceAgencyReceivableGross|
| &#128270;  | ClusteredIndex | ON Job\_PriceAgencyReceivableNet|
| &#128270;  | ClusteredIndex | ON Job\_PriceAgencyReceivableTax|
| &#128270;  | ClusteredIndex | ON Job\_QuotedPriceAgencyPayableGross|
| &#128270;  | ClusteredIndex | ON Job\_QuotedPriceAgencyPayableNet|
| &#128270;  | ClusteredIndex | ON Job\_QuotedPriceAgencyPayableTax|
| &#128270;  | ClusteredIndex | ON Job\_QuotedPriceAgencyReceivableGross|
| &#128270;  | ClusteredIndex | ON Job\_QuotedPriceAgencyReceivableNet|
| &#128270;  | ClusteredIndex | ON Job\_QuotedPriceAgencyReceivableTax|
| &#128270;  | ClusteredIndex | ON Job\_StartDate|
| &#128270;  | ClusteredIndex | ON Job\_TenantAcceptedStartDate|
| &#128270;  | ClusteredIndex | ON Job\_TenantNotes|
| &#128270;  | ClusteredIndex | ON Job\_UpdateDate|
| &#128270;  | ClusteredIndex | ON Job\_WorksExpiryDate|
| &#128270;  | ClusteredIndex | ON Landlord\_Address\_AddressLine1|
| &#128270;  | ClusteredIndex | ON Landlord\_Address\_AddressLine2|
| &#128270;  | ClusteredIndex | ON Landlord\_Address\_Country|
| &#128270;  | ClusteredIndex | ON Landlord\_Address\_County|
| &#128270;  | ClusteredIndex | ON Landlord\_Address\_PostCode|
| &#128270;  | ClusteredIndex | ON Landlord\_Address\_Town|
| &#128270;  | ClusteredIndex | ON Landlord\_AssignedAgent|
| &#128270;  | ClusteredIndex | ON Landlord\_Brand|
| &#128270;  | ClusteredIndex | ON Landlord\_CompanyName|
| &#128270;  | ClusteredIndex | ON Landlord\_ContactNumber|
| &#128270;  | ClusteredIndex | ON Landlord\_ContactNumberAlt|
| &#128270;  | ClusteredIndex | ON Landlord\_DisplayName|
| &#128270;  | ClusteredIndex | ON Landlord\_EmailAddress|
| &#128270;  | ClusteredIndex | ON Landlord\_EmailCC|
| &#128270;  | ClusteredIndex | ON Landlord\_ExternalRef|
| &#128270;  | ClusteredIndex | ON Landlord\_FirstName|
| &#128270;  | ClusteredIndex | ON Landlord\_Id|
| &#128270;  | ClusteredIndex | ON Landlord\_IsDeleted|
| &#128270;  | ClusteredIndex | ON Landlord\_Surname|
| &#128270;  | ClusteredIndex | ON Landlord\_Title|
| &#128270;  | ClusteredIndex | ON Landlord\_UpdateDate|
| &#128270;  | ClusteredIndex | ON Landlord\_WorksAuthorisationLimit|
| &#128270;  | ClusteredIndex | ON Media|
| &#128270;  | ClusteredIndex | ON Property\_Address\_AddressLine1|
| &#128270;  | ClusteredIndex | ON Property\_Address\_AddressLine2|
| &#128270;  | ClusteredIndex | ON Property\_Address\_Country|
| &#128270;  | ClusteredIndex | ON Property\_Address\_County|
| &#128270;  | ClusteredIndex | ON Property\_Address\_PostCode|
| &#128270;  | ClusteredIndex | ON Property\_Address\_Town|
| &#128270;  | ClusteredIndex | ON Property\_ArchiveStatus|
| &#128270;  | ClusteredIndex | ON Property\_AssignedAgent|
| &#128270;  | ClusteredIndex | ON Property\_AssignedTeam|
| &#128270;  | ClusteredIndex | ON Property\_BlockId|
| &#128270;  | ClusteredIndex | ON Property\_Brand|
| &#128270;  | ClusteredIndex | ON Property\_Created|
| &#128270;  | ClusteredIndex | ON Property\_ExternalPropertyRef|
| &#128270;  | ClusteredIndex | ON Property\_Id|
| &#128270;  | ClusteredIndex | ON Property\_IsDeleted|
| &#128270;  | ClusteredIndex | ON Property\_IsNotManaged|
| &#128270;  | ClusteredIndex | ON Property\_KeyReference|
| &#128270;  | ClusteredIndex | ON Property\_PropertyAddressId|
| &#128270;  | ClusteredIndex | ON Property\_PropertyManager|
| &#128270;  | ClusteredIndex | ON Property\_UpdateDate|
| &#128270;  | ClusteredIndex | ON Property\_Warranties|
| &#128270;  | ClusteredIndex | ON PropertyAddressId|
| &#128270;  | ClusteredIndex | ON QuoteEndTime|
| &#128270;  | ClusteredIndex | ON QuoteNotes|
| &#128270;  | ClusteredIndex | ON QuoteRequests|
| &#128270;  | ClusteredIndex | ON Quotes|
| &#128270;  | ClusteredIndex | ON RaisedByAgent\_Brand|
| &#128270;  | ClusteredIndex | ON RaisedByAgent\_ContactNo|
| &#128270;  | ClusteredIndex | ON RaisedByAgent\_DisplayName|
| &#128270;  | ClusteredIndex | ON RaisedByAgent\_EmailAddress|
| &#128270;  | ClusteredIndex | ON RaisedByAgent\_EmailCC|
| &#128270;  | ClusteredIndex | ON RaisedByAgent\_ExternalRef|
| &#128270;  | ClusteredIndex | ON RaisedByAgent\_Id|
| &#128270;  | ClusteredIndex | ON RaisedByAgent\_IsDeleted|
| &#128270;  | ClusteredIndex | ON RaisedByAgent\_UpdateDate|
| &#128270;  | ClusteredIndex | ON Reporter\_Id|
| &#128270;  | ClusteredIndex | ON Reporter\_Role|
| &#128270;  | ClusteredIndex | ON Salutation|
| &#128270;  | ClusteredIndex | ON ServiceEventId|
| &#128270;  | ClusteredIndex | ON Status|
| &#128270;  | ClusteredIndex | ON StatusChanged|
| &#128270;  | ClusteredIndex | ON Surname|
| &#128270;  | ClusteredIndex | ON TenantAcceptComplete|
| &#128270;  | ClusteredIndex | ON TenantId|
| &#128270;  | ClusteredIndex | ON TenantNotes|
| &#128270;  | ClusteredIndex | ON TenantPresenceRequested|
| &#128270;  | ClusteredIndex | ON TermsAccepted|
| &#128270;  | ClusteredIndex | ON Title|
| &#128270;  | ClusteredIndex | ON VulnerableOccupiers|
| &#128270;  | ClusteredIndex | ON WorksAuthorisationLimit|
| &#128270;  | ClusteredIndex | ON WorksPaidBy|
| &#128270;  | ClusteredIndex | ON \_meta\_source\_file\_name|
| &#128270;  | ClusteredIndex | ON \_meta\_source\_file\_path|
| &#128270;  | ClusteredIndex | ON \_meta\_raw\_row\_number|
| &#128270;  | ClusteredIndex | ON \_meta\_row\_hash|
| &#128270;  | ClusteredIndex | ON \_meta\_pipeline\_id|
| &#128270;  | ClusteredIndex | ON \_meta\_ingest\_ts|



### Table FixFlo.Landlord 
|Idx |Name |Data Type |
|---|---|---|
| &#128270; | Address\_AddressLine1| varchar(8000)  |
| &#128270; | Address\_AddressLine2| varchar(8000)  |
| &#128270; | Address\_Country| varchar(8000)  |
| &#128270; | Address\_County| varchar(8000)  |
| &#128270; | Address\_PostCode| varchar(8000)  |
| &#128270; | Address\_Town| varchar(8000)  |
| &#128270; | AssignedAgent| varchar(8000)  |
| &#128270; | Brand| varchar(8000)  |
| &#128270; | CompanyName| varchar(8000)  |
| &#128270; | ContactNumber| varchar(8000)  |
| &#128270; | ContactNumberAlt| varchar(8000)  |
| &#128270; | DisplayName| varchar(8000)  |
| &#128270; | EmailAddress| varchar(8000)  |
| &#128270; | EmailCC| varchar(8000)  |
| &#128270; | ExternalRef| varchar(8000)  |
| &#128270; | FirstName| varchar(8000)  |
| &#128270; | Id| varchar(8000)  |
| &#128270; | IngestedUTC| varchar(8000)  |
| &#128270; | IsDeleted| bit  |
| &#128270; | Surname| varchar(8000)  |
| &#128270; | Title| varchar(8000)  |
| &#128270; | UpdateDate| varchar(8000)  |
| &#128270; | WorksAuthorisationLimit| varchar(8000)  |
| &#128270; | \_source\_page| bigint  |
| &#128270; | \_meta\_source\_file\_name| varchar(8000)  |
| &#128270; | \_meta\_source\_file\_path| varchar(8000)  |
| &#128270; | \_meta\_raw\_row\_number| int  |
| &#128270; | \_meta\_row\_hash| varchar(8000)  |
| &#128270; | \_meta\_pipeline\_id| varchar(8000)  |
| &#128270; | \_meta\_ingest\_ts| datetime2(26)  |


##### Indexes 
|Type |Name |On |
|---|---|---|
| &#128270;  | ClusteredIndex | ON Address\_AddressLine1|
| &#128270;  | ClusteredIndex | ON Address\_AddressLine2|
| &#128270;  | ClusteredIndex | ON Address\_Country|
| &#128270;  | ClusteredIndex | ON Address\_County|
| &#128270;  | ClusteredIndex | ON Address\_PostCode|
| &#128270;  | ClusteredIndex | ON Address\_Town|
| &#128270;  | ClusteredIndex | ON AssignedAgent|
| &#128270;  | ClusteredIndex | ON Brand|
| &#128270;  | ClusteredIndex | ON CompanyName|
| &#128270;  | ClusteredIndex | ON ContactNumber|
| &#128270;  | ClusteredIndex | ON ContactNumberAlt|
| &#128270;  | ClusteredIndex | ON DisplayName|
| &#128270;  | ClusteredIndex | ON EmailAddress|
| &#128270;  | ClusteredIndex | ON EmailCC|
| &#128270;  | ClusteredIndex | ON ExternalRef|
| &#128270;  | ClusteredIndex | ON FirstName|
| &#128270;  | ClusteredIndex | ON Id|
| &#128270;  | ClusteredIndex | ON IngestedUTC|
| &#128270;  | ClusteredIndex | ON IsDeleted|
| &#128270;  | ClusteredIndex | ON Surname|
| &#128270;  | ClusteredIndex | ON Title|
| &#128270;  | ClusteredIndex | ON UpdateDate|
| &#128270;  | ClusteredIndex | ON WorksAuthorisationLimit|
| &#128270;  | ClusteredIndex | ON \_source\_page|
| &#128270;  | ClusteredIndex | ON \_meta\_source\_file\_name|
| &#128270;  | ClusteredIndex | ON \_meta\_source\_file\_path|
| &#128270;  | ClusteredIndex | ON \_meta\_raw\_row\_number|
| &#128270;  | ClusteredIndex | ON \_meta\_row\_hash|
| &#128270;  | ClusteredIndex | ON \_meta\_pipeline\_id|
| &#128270;  | ClusteredIndex | ON \_meta\_ingest\_ts|



### Table FixFlo.Leaseholder 
|Idx |Name |Data Type |
|---|---|---|
| &#128270; | Address\_AddressLine1| varchar(8000)  |
| &#128270; | Address\_AddressLine2| varchar(8000)  |
| &#128270; | Address\_Country| varchar(8000)  |
| &#128270; | Address\_County| varchar(8000)  |
| &#128270; | Address\_PostCode| varchar(8000)  |
| &#128270; | Address\_Town| varchar(8000)  |
| &#128270; | AuthUserId| bigint  |
| &#128270; | Brand\_Id| varchar(8000)  |
| &#128270; | Brand\_Name| varchar(8000)  |
| &#128270; | CompanyName| varchar(8000)  |
| &#128270; | ContactNumber| varchar(8000)  |
| &#128270; | ContactNumberAlt| varchar(8000)  |
| &#128270; | DisplayName| varchar(8000)  |
| &#128270; | EmailAddress| varchar(8000)  |
| &#128270; | EmailCC| varchar(8000)  |
| &#128270; | ExternalLeaseholderRef| varchar(8000)  |
| &#128270; | FirstName| varchar(8000)  |
| &#128270; | Id| varchar(8000)  |
| &#128270; | IngestedUTC| varchar(8000)  |
| &#128270; | IsDeleted| bit  |
| &#128270; | Surname| varchar(8000)  |
| &#128270; | Title| varchar(8000)  |
| &#128270; | UpdateDate| varchar(8000)  |
| &#128270; | \_source\_page| bigint  |
| &#128270; | \_meta\_source\_file\_name| varchar(8000)  |
| &#128270; | \_meta\_source\_file\_path| varchar(8000)  |
| &#128270; | \_meta\_raw\_row\_number| int  |
| &#128270; | \_meta\_row\_hash| varchar(8000)  |
| &#128270; | \_meta\_pipeline\_id| varchar(8000)  |
| &#128270; | \_meta\_ingest\_ts| datetime2(26)  |
| &#128270; | Brand| varchar(8000)  |


##### Indexes 
|Type |Name |On |
|---|---|---|
| &#128270;  | ClusteredIndex | ON Address\_AddressLine1|
| &#128270;  | ClusteredIndex | ON Address\_AddressLine2|
| &#128270;  | ClusteredIndex | ON Address\_Country|
| &#128270;  | ClusteredIndex | ON Address\_County|
| &#128270;  | ClusteredIndex | ON Address\_PostCode|
| &#128270;  | ClusteredIndex | ON Address\_Town|
| &#128270;  | ClusteredIndex | ON AuthUserId|
| &#128270;  | ClusteredIndex | ON Brand\_Id|
| &#128270;  | ClusteredIndex | ON Brand\_Name|
| &#128270;  | ClusteredIndex | ON CompanyName|
| &#128270;  | ClusteredIndex | ON ContactNumber|
| &#128270;  | ClusteredIndex | ON ContactNumberAlt|
| &#128270;  | ClusteredIndex | ON DisplayName|
| &#128270;  | ClusteredIndex | ON EmailAddress|
| &#128270;  | ClusteredIndex | ON EmailCC|
| &#128270;  | ClusteredIndex | ON ExternalLeaseholderRef|
| &#128270;  | ClusteredIndex | ON FirstName|
| &#128270;  | ClusteredIndex | ON Id|
| &#128270;  | ClusteredIndex | ON IngestedUTC|
| &#128270;  | ClusteredIndex | ON IsDeleted|
| &#128270;  | ClusteredIndex | ON Surname|
| &#128270;  | ClusteredIndex | ON Title|
| &#128270;  | ClusteredIndex | ON UpdateDate|
| &#128270;  | ClusteredIndex | ON \_source\_page|
| &#128270;  | ClusteredIndex | ON \_meta\_source\_file\_name|
| &#128270;  | ClusteredIndex | ON \_meta\_source\_file\_path|
| &#128270;  | ClusteredIndex | ON \_meta\_raw\_row\_number|
| &#128270;  | ClusteredIndex | ON \_meta\_row\_hash|
| &#128270;  | ClusteredIndex | ON \_meta\_pipeline\_id|
| &#128270;  | ClusteredIndex | ON \_meta\_ingest\_ts|
| &#128270;  | ClusteredIndex | ON Brand|



### Table FixFlo.Property 
|Idx |Name |Data Type |
|---|---|---|
| &#128270; | Address\_AddressLine1| varchar(8000)  |
| &#128270; | Address\_AddressLine2| varchar(8000)  |
| &#128270; | Address\_Country| varchar(8000)  |
| &#128270; | Address\_County| varchar(8000)  |
| &#128270; | Address\_PostCode| varchar(8000)  |
| &#128270; | Address\_Town| varchar(8000)  |
| &#128270; | ArchiveStatus| varchar(8000)  |
| &#128270; | AssignedAgent| varchar(8000)  |
| &#128270; | AssignedTeam| varchar(8000)  |
| &#128270; | BlockId| bigint  |
| &#128270; | Brand\_Id| varchar(8000)  |
| &#128270; | Brand\_Name| varchar(8000)  |
| &#128270; | Created| varchar(8000)  |
| &#128270; | ExternalPropertyRef| varchar(8000)  |
| &#128270; | Id| bigint  |
| &#128270; | IngestedUTC| varchar(8000)  |
| &#128270; | IsDeleted| bit  |
| &#128270; | IsNotManaged| bit  |
| &#128270; | KeyReference| varchar(8000)  |
| &#128270; | PropertyAddressId| bigint  |
| &#128270; | PropertyManager| varchar(8000)  |
| &#128270; | UpdateDate| varchar(8000)  |
| &#128270; | Warranties| varchar(8000)  |
| &#128270; | \_source\_page| bigint  |
| &#128270; | \_meta\_source\_file\_name| varchar(8000)  |
| &#128270; | \_meta\_source\_file\_path| varchar(8000)  |
| &#128270; | \_meta\_raw\_row\_number| int  |
| &#128270; | \_meta\_row\_hash| varchar(8000)  |
| &#128270; | \_meta\_pipeline\_id| varchar(8000)  |
| &#128270; | \_meta\_ingest\_ts| datetime2(26)  |
| &#128270; | Brand| varchar(8000)  |


##### Indexes 
|Type |Name |On |
|---|---|---|
| &#128270;  | ClusteredIndex | ON Address\_AddressLine1|
| &#128270;  | ClusteredIndex | ON Address\_AddressLine2|
| &#128270;  | ClusteredIndex | ON Address\_Country|
| &#128270;  | ClusteredIndex | ON Address\_County|
| &#128270;  | ClusteredIndex | ON Address\_PostCode|
| &#128270;  | ClusteredIndex | ON Address\_Town|
| &#128270;  | ClusteredIndex | ON ArchiveStatus|
| &#128270;  | ClusteredIndex | ON AssignedAgent|
| &#128270;  | ClusteredIndex | ON AssignedTeam|
| &#128270;  | ClusteredIndex | ON BlockId|
| &#128270;  | ClusteredIndex | ON Brand\_Id|
| &#128270;  | ClusteredIndex | ON Brand\_Name|
| &#128270;  | ClusteredIndex | ON Created|
| &#128270;  | ClusteredIndex | ON ExternalPropertyRef|
| &#128270;  | ClusteredIndex | ON Id|
| &#128270;  | ClusteredIndex | ON IngestedUTC|
| &#128270;  | ClusteredIndex | ON IsDeleted|
| &#128270;  | ClusteredIndex | ON IsNotManaged|
| &#128270;  | ClusteredIndex | ON KeyReference|
| &#128270;  | ClusteredIndex | ON PropertyAddressId|
| &#128270;  | ClusteredIndex | ON PropertyManager|
| &#128270;  | ClusteredIndex | ON UpdateDate|
| &#128270;  | ClusteredIndex | ON Warranties|
| &#128270;  | ClusteredIndex | ON \_source\_page|
| &#128270;  | ClusteredIndex | ON \_meta\_source\_file\_name|
| &#128270;  | ClusteredIndex | ON \_meta\_source\_file\_path|
| &#128270;  | ClusteredIndex | ON \_meta\_raw\_row\_number|
| &#128270;  | ClusteredIndex | ON \_meta\_row\_hash|
| &#128270;  | ClusteredIndex | ON \_meta\_pipeline\_id|
| &#128270;  | ClusteredIndex | ON \_meta\_ingest\_ts|
| &#128270;  | ClusteredIndex | ON Brand|



### Table FixFlo.Tenant 
|Idx |Name |Data Type |
|---|---|---|
| &#128270; | Address\_AddressLine1| varchar(8000)  |
| &#128270; | Address\_AddressLine2| varchar(8000)  |
| &#128270; | Address\_Country| varchar(8000)  |
| &#128270; | Address\_County| varchar(8000)  |
| &#128270; | Address\_PostCode| varchar(8000)  |
| &#128270; | Address\_Town| varchar(8000)  |
| &#128270; | Brand\_Id| varchar(8000)  |
| &#128270; | Brand\_Name| varchar(8000)  |
| &#128270; | CompanyName| varchar(8000)  |
| &#128270; | ContactNumber| varchar(8000)  |
| &#128270; | ContactNumberAlt| varchar(8000)  |
| &#128270; | DisplayName| varchar(8000)  |
| &#128270; | EmailAddress| varchar(8000)  |
| &#128270; | EmailCC| varchar(8000)  |
| &#128270; | ExternalPropertyRef| varchar(8000)  |
| &#128270; | ExternalRef| varchar(8000)  |
| &#128270; | FirstName| varchar(8000)  |
| &#128270; | Id| varchar(8000)  |
| &#128270; | IngestedUTC| varchar(8000)  |
| &#128270; | IsAnonymised| bit  |
| &#128270; | IsDeleted| bit  |
| &#128270; | Surname| varchar(8000)  |
| &#128270; | Title| varchar(8000)  |
| &#128270; | UpdateDate| varchar(8000)  |
| &#128270; | \_source\_page| bigint  |
| &#128270; | \_meta\_source\_file\_name| varchar(8000)  |
| &#128270; | \_meta\_source\_file\_path| varchar(8000)  |
| &#128270; | \_meta\_raw\_row\_number| int  |
| &#128270; | \_meta\_row\_hash| varchar(8000)  |
| &#128270; | \_meta\_pipeline\_id| varchar(8000)  |
| &#128270; | \_meta\_ingest\_ts| datetime2(26)  |
| &#128270; | Brand| varchar(8000)  |


##### Indexes 
|Type |Name |On |
|---|---|---|
| &#128270;  | ClusteredIndex | ON Address\_AddressLine1|
| &#128270;  | ClusteredIndex | ON Address\_AddressLine2|
| &#128270;  | ClusteredIndex | ON Address\_Country|
| &#128270;  | ClusteredIndex | ON Address\_County|
| &#128270;  | ClusteredIndex | ON Address\_PostCode|
| &#128270;  | ClusteredIndex | ON Address\_Town|
| &#128270;  | ClusteredIndex | ON Brand\_Id|
| &#128270;  | ClusteredIndex | ON Brand\_Name|
| &#128270;  | ClusteredIndex | ON CompanyName|
| &#128270;  | ClusteredIndex | ON ContactNumber|
| &#128270;  | ClusteredIndex | ON ContactNumberAlt|
| &#128270;  | ClusteredIndex | ON DisplayName|
| &#128270;  | ClusteredIndex | ON EmailAddress|
| &#128270;  | ClusteredIndex | ON EmailCC|
| &#128270;  | ClusteredIndex | ON ExternalPropertyRef|
| &#128270;  | ClusteredIndex | ON ExternalRef|
| &#128270;  | ClusteredIndex | ON FirstName|
| &#128270;  | ClusteredIndex | ON Id|
| &#128270;  | ClusteredIndex | ON IngestedUTC|
| &#128270;  | ClusteredIndex | ON IsAnonymised|
| &#128270;  | ClusteredIndex | ON IsDeleted|
| &#128270;  | ClusteredIndex | ON Surname|
| &#128270;  | ClusteredIndex | ON Title|
| &#128270;  | ClusteredIndex | ON UpdateDate|
| &#128270;  | ClusteredIndex | ON \_source\_page|
| &#128270;  | ClusteredIndex | ON \_meta\_source\_file\_name|
| &#128270;  | ClusteredIndex | ON \_meta\_source\_file\_path|
| &#128270;  | ClusteredIndex | ON \_meta\_raw\_row\_number|
| &#128270;  | ClusteredIndex | ON \_meta\_row\_hash|
| &#128270;  | ClusteredIndex | ON \_meta\_pipeline\_id|
| &#128270;  | ClusteredIndex | ON \_meta\_ingest\_ts|
| &#128270;  | ClusteredIndex | ON Brand|




## View DIM_DATE_VW

Query DIM_DATE_VW
```
/*
select count(*) as num\_rows from [FixFlo].[DIM\_DATE\_VW];
select top 100 * from [FixFlo].[DIM\_DATE\_VW];
select * from [FixFlo].[DIM\_DATE\_FISCAL\_PERIOD\_VW] order by Fiscal\_Year, Fiscal\_Period;

*/

CREATE     VIEW [FixFlo].[DIM\_DATE\_VW] as 

WITH	cte\_FYStart as (select 4 as FYStartMonth)
,		cte\_Min as (select CONVERT(DATE, '2020-04-01') as MinDate)
,		cte\_Max AS    
-- End of Current Fiscal Year
(
	SELECT	EOMONTH (
				DATEFROMPARTS (
					YEAR(GETDATE())
                    + CASE WHEN s.FYStartMonth = 1 THEN 0 WHEN MONTH(GETDATE()) &gt;= s.FYStartMonth THEN 1 ELSE 0 END
					,    CASE WHEN s.FYStartMonth = 1 THEN 12 ELSE s.FYStartMonth - 1 END
                    ,    1
				)
			) AS MaxDate
        FROM    cte\_FYStart s
)
,		cte\_Nbr as (select DATEDIFF(day, MinDate, MaxDate) + 1 as Nbr  from cte\_Min cross join cte\_Max)
,		cte\_Exp00(Nbr) AS (SELECT 1 UNION ALL SELECT 1)
,		cte\_Exp02(Nbr) AS (SELECT 1 FROM cte\_Exp00 AS a, cte\_Exp00 AS b)
,		cte\_Exp04(Nbr) AS (SELECT 1 FROM cte\_Exp02 AS a, cte\_Exp02 AS b)
,		cte\_Exp08(Nbr) AS (SELECT 1 FROM cte\_Exp04 AS a, cte\_Exp04 AS b)
,		cte\_Exp16(Nbr) AS (SELECT 1 FROM cte\_Exp08 AS a, cte\_Exp08 AS b)
,		cte\_Exp32(Nbr) AS (SELECT 1 FROM cte\_Exp16 AS a, cte\_Exp16 AS b)
,		cte\_Tally(Nbr) AS (SELECT ROW\_NUMBER() OVER (ORDER BY (SELECT NULL)) FROM cte\_Exp32)
,		cte\_Date(Date) AS (SELECT DATEADD(DAY,t.Nbr - 1, m.MinDate) FROM cte\_Tally t cross join cte\_Min m cross join cte\_Nbr n WHERE t.Nbr &lt;= n.Nbr)

SELECT	d.[Date]

    -- Pre-calculated calendar parts
,		cal.[Year]
,		cal.[Month]
,		cal.[Day]
,		cal.Date\_Number

,		cal.Month\_Name
,		cal.Month\_Name\_Long

,		cal.Month\_Starting
,		cal.Month\_Ending
,		cal.Month\_Offset

,		pm.Previous\_Month\_Starting
,		pm.Previous\_Month\_Ending

,		cal.Quarter\_Number
,		cal.[Quarter]
,		cal.Year\_Quarter

,		cal.Day\_Name
,		cal.Day\_Name\_Long
,		cal.Day\_Name\_Initial
,		cal.Day\_Name\_Sort
,		cal.[DayOfYear]

,		cal.[Week]
,		cal.[ISO\_Week]

    -- Fiscal
,		fy.Fiscal\_Year
,		fy.Fiscal\_Year\_Name
,		fy.Fiscal\_Period
,		cal.Month\_Name\_Long AS Financial\_Period\_Name
,		fy.Fiscal\_Period\_Sort
,		fy.Fiscal\_Quarter\_Number
,		fy.Fiscal\_Quarter
,		fy.Fiscal\_Year\_Quarter
,		fy.Fiscal\_Year\_Starting
,		fy.Fiscal\_Year\_Ending
,		DATEPART(DAYOFYEAR, fbase.Shifted\_Date) AS Fiscal\_Day\_Of\_Year

FROM    cte\_Date d
CROSS JOIN cte\_FYStart s

-- ✅ Calendar calc once
CROSS APPLY
(
    SELECT	YEAR(d.[Date]) AS [Year]
	,		MONTH(d.[Date]) AS [Month]
	,		DAY(d.[Date]) AS [Day]
	,		YEAR(d.[Date]) * 10000 + MONTH(d.[Date]) * 100 + DAY(d.[Date]) AS Date\_Number

	,		LEFT(DATENAME(MONTH, d.[Date]), 3) AS Month\_Name
	,		DATENAME(MONTH, d.[Date]) AS Month\_Name\_Long
	,		LEFT(DATENAME(MONTH, d.[Date]), 3) AS Month\_Name\_Short
	,		LEFT(DATENAME(MONTH, d.[Date]), 1) AS Month\_Name\_Initial
	,		convert(date, DATEADD(MONTH, DATEDIFF(MONTH, 0, d.[Date]), 0)) AS Month\_Starting
	,		EOMONTH(d.[Date]) AS Month\_Ending
	
	,		(DATEPART(YEAR, d.[Date]) * 12 + DATEPART(MONTH, d.[Date]))
				- (DATEPART(YEAR, GETDATE()) * 12 + DATEPART(MONTH, GETDATE())) AS Month\_Offset

	,		DATEPART(QUARTER, d.[Date]) AS Quarter\_Number
	,		CONCAT('Q', DATEPART(QUARTER, d.[Date])) AS Quarter
	,		CONCAT(YEAR(d.[Date]), '-Q', DATEPART(QUARTER, d.[Date])) AS Year\_Quarter

	,		LEFT(DATENAME(WEEKDAY, d.[Date]), 3) AS Day\_Name
	,		DATENAME(WEEKDAY, d.[Date]) AS Day\_Name\_Long
	,		LEFT(DATENAME(WEEKDAY, d.[Date]), 3) AS Day\_Name\_Short
	,		LEFT(DATENAME(WEEKDAY, d.[Date]), 1) AS Day\_Name\_Initial
	,		((DATEPART(DW, d.[Date]) + @@DATEFIRST + 5) % 7) + 1 AS Day\_Name\_Sort
	,		DATEPART(DAYOFYEAR, d.[Date]) AS DayOfYear

	,		DATEPART(WEEK, d.[Date]) AS [Week]
	,		DATEPART(ISOWK, d.[Date]) AS [ISO\_Week]
) cal

-- ✅ Previous month calc once
CROSS APPLY
(
    SELECT	convert(date, DATEADD(MONTH, DATEDIFF(MONTH, 0, GETDATE()) - 1, 0)) AS Previous\_Month\_Starting
	,		EOMONTH(GETDATE(), -1) AS Previous\_Month\_Ending
) pm

-- ✅ Fiscal shift only once
CROSS APPLY
(
    SELECT	DATEADD(MONTH, 1 - s.FYStartMonth, d.[Date]) AS Shifted\_Date
	,		((cal.[Month] - s.FYStartMonth + 12) % 12) + 1 AS Fiscal\_Period
	,		((cal.[Month] - s.FYStartMonth + 12) % 12) + 1 AS Fiscal\_Period\_Sort
) fbase

-- ✅ Fiscal derivations
CROSS APPLY
(
    SELECT	YEAR(DATEADD(YEAR, 1, fbase.Shifted\_Date)) AS Fiscal\_Year
	,		CONCAT( YEAR(fbase.Shifted\_Date), '-', YEAR(fbase.Shifted\_Date) + 1) AS Fiscal\_Year\_Name
	,		fbase.Fiscal\_Period
	,		fbase.Fiscal\_Period\_Sort
	,		((fbase.Fiscal\_Period - 1) / 3) + 1 AS Fiscal\_Quarter\_Number
	,		CONCAT('Q', ((fbase.Fiscal\_Period - 1) / 3) + 1) AS Fiscal\_Quarter
	,		CONCAT(YEAR(DATEADD(YEAR, 1, fbase.Shifted\_Date)), '-Q', ((fbase.Fiscal\_Period - 1) / 3) + 1) AS Fiscal\_Year\_Quarter
	,		DATEFROMPARTS(YEAR(fbase.Shifted\_Date), s.FYStartMonth, 1) AS Fiscal\_Year\_Starting
	,		DATEADD(DAY, -1, DATEADD(YEAR, 1, DATEFROMPARTS(YEAR(fbase.Shifted\_Date), s.FYStartMonth, 1))) AS Fiscal\_Year\_Ending
) fy

```

|Idx |Name |Type |
|---|---|---|
|  | Date| date  |
|  | Year| int  |
|  | Month| int  |
|  | Day| int  |
|  | Date\_Number| int  |
|  | Month\_Name| nvarchar(3)  |
|  | Month\_Name\_Long| nvarchar(30)  |
|  | Month\_Starting| date  |
|  | Month\_Ending| date  |
|  | Month\_Offset| int  |
|  | Previous\_Month\_Starting| date  |
|  | Previous\_Month\_Ending| date  |
|  | Quarter\_Number| int  |
| * | Quarter| varchar(13)  |
| * | Year\_Quarter| varchar(26)  |
|  | Day\_Name| nvarchar(3)  |
|  | Day\_Name\_Long| nvarchar(30)  |
|  | Day\_Name\_Initial| nvarchar(1)  |
|  | Day\_Name\_Sort| int  |
|  | DayOfYear| int  |
|  | Week| int  |
|  | ISO\_Week| int  |
|  | Fiscal\_Year| int  |
| * | Fiscal\_Year\_Name| varchar(25)  |
|  | Fiscal\_Period| int  |
|  | Financial\_Period\_Name| nvarchar(30)  |
|  | Fiscal\_Period\_Sort| int  |
|  | Fiscal\_Quarter\_Number| int  |
| * | Fiscal\_Quarter| varchar(13)  |
| * | Fiscal\_Year\_Quarter| varchar(26)  |
|  | Fiscal\_Year\_Starting| date  |
|  | Fiscal\_Year\_Ending| date  |
|  | Fiscal\_Day\_Of\_Year| int  |


