#!/usr/bin/env python
# coding: utf-8

# ## nb_supfam_dataset_curation_v4
# 
# New notebook

# In[4]:


spark.sql("CREATE SCHEMA IF NOT EXISTS cdm")
spark.sql("CREATE SCHEMA IF NOT EXISTS cdm_ext")


# In[7]:


df = spark.sql("""
SELECT
    dim_sc_school_id AS SchoolId
FROM lh_data_platform_bronze.education.dim_sc_school
""")

(
    df.write
      .format("delta")
      .mode("overwrite")
      .option("overwriteSchema","true")
      .saveAsTable("cdm.school")
)


# In[1]:


#!/usr/bin/env python
# coding: utf-8

# ## nb_supfam_dataset_curation_v3
# 
# New notebook

# In[2]:


from delta.tables import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
from pyspark.sql.functions import (
    lit, row_number, current_timestamp, col, when, concat_ws, to_json, sha2
    )

spark.conf.set("spark.sql.legacy.parquet.int96RebaseModeInRead","CORRECTED")
spark.conf.set("spark.sql.legacy.parquet.int96RebaseModeInWrite","CORRECTED")
spark.conf.set("spark.sql.legacy.parquet.datetimeRebaseModeInRead","CORRECTED")
spark.conf.set("spark.sql.legacy.parquet.datetimeRebaseModeInWrite","CORRECTED")
spark.conf.set('spark.databricks.delta.schema.autoMerge.enabled', 'true')

def OverwriteLoad(
    df,
    targetPath: str,
    targetTable: str,
    partitionByCols: list = [],
    zOrderByCols: list = []
):

    # overwrites target

    (
        df
            .write
            .format('delta')
            .mode('overwrite')
            .option('overwriteSchema', 'true')
            .partitionBy(*partitionByCols)
            .saveAsTable(f'{targetTable}')
    )

    if zOrderByCols:
        (
            DeltaTable
                .forPath(spark, targetPath)
                .optimize()
                .executeZOrderBy(*zOrderByCols)
        )


# In[2]:


spark.sql(f'CREATE DATABASE IF NOT EXISTS cdm')
spark.sql(f'CREATE DATABASE IF NOT EXISTS cdm_ext')


# In[3]:


df = spark.sql("""
    SELECT
        DIM_SC_SCHOOL_ID AS SchoolId
    FROM education.DIM_SC_SCHOOL
""")

OverwriteLoad(
    df,
    'Tables/cdm/school',
    'cdm.school'
)


# In[4]:


df = spark.sql("""
    SELECT 
        dp.LEGACY_ID as PersonID, 
        fmp.FACT_MISSING_PERSON_ID as MfHEpisodeID, 
        fmp.START_DTTM as MfHStartDate, 
        fmp.END_DTTM as MfHEndDate 
    FROM child_social.DIM_PERSON dp 
    INNER JOIN child_social.fact_missing_person fmp ON dp.dim_person_id = fmp.dim_person_id
""")

OverwriteLoad(
    df,
    'Tables/cdm/mfh_episode',
    'cdm.mfh_episode'
)


# In[5]:


df = spark.sql("""
    SELECT DISTINCT
        dp.LEGACY_ID AS PersonID, 
        fcps.FACT_CARE_PLAN_SUMMARY_ID AS CINEpisodeID, 
        TO_DATE(fcps.START_DTTM, 'yyyy-MM-dd HH:mm:ss') AS CINStartDate,
        TO_DATE(fcps.END_DTTM, 'yyyy-MM-dd HH:mm:ss') AS CINEndDate,
        CASE 
            WHEN fr.group_referral_id IS NULL THEN 
                concat_ws(
                '', 
                'CIN', 
                CAST(fr.dim_person_id AS STRING), 
                date_format(to_timestamp(fcps.START_DTTM, 'yyyy-MM-dd HH:mm:ss'), 'yyyyMMdd')
                )
            ELSE 
                concat_ws(
                '', 
                'CIN', 
                CAST(fr.group_referral_id AS STRING), 
                date_format(to_timestamp(fcps.START_DTTM, 'yyyy-MM-dd HH:mm:ss'), 'yyyyMMdd')
                )
        END AS GroupID
    FROM child_social.DIM_PERSON AS dp 
    JOIN child_social.FACT_CARE_PLAN_SUMMARY AS fcps ON dp.dim_person_id = fcps.dim_person_id 
    JOIN child_social.FACT_REFERRALS AS fr ON dp.dim_person_id = fr.dim_person_id
""")

OverwriteLoad(
    df,
    'Tables/cdm/cin_episode',
    'cdm.cin_episode'
)


# In[6]:


df = spark.sql("""
    SELECT DISTINCT
        dp.LEGACY_ID AS PersonID, 
        fcl.FACT_CLA_ID as CLAEpisodeID,
        TO_DATE(fcl.START_DTTM, 'yyyy-MM-dd HH:mm:ss') AS CLAStartDate,
        TO_DATE(fcl.END_DTTM, 'yyyy-MM-dd HH:mm:ss') AS CLAEndDate,
        CASE 
            WHEN fr.group_referral_id IS NULL THEN 
                concat_ws(
                '', 
                'CLA', 
                CAST(fr.dim_person_id AS STRING), 
                date_format(to_timestamp(fcl.START_DTTM, 'yyyy-MM-dd HH:mm:ss'), 'yyyyMMdd')
                )
            ELSE 
                concat_ws(
                '', 
                'CLA', 
                CAST(fr.group_referral_id AS STRING), 
                date_format(to_timestamp(fcl.START_DTTM, 'yyyy-MM-dd HH:mm:ss'), 'yyyyMMdd')
                )
        END AS GroupID
    FROM child_social.DIM_PERSON AS dp 
    JOIN child_social.FACT_CLA AS fcl ON dp.dim_person_id = fcl.dim_person_id 
    JOIN child_social.FACT_REFERRALS AS fr ON dp.dim_person_id = fr.dim_person_id
""")

OverwriteLoad(
    df,
    'Tables/cdm/cla_episode',
    'cdm.cla_episode'
)


# In[7]:


df = spark.sql("""
    SELECT DISTINCT
        dp.LEGACY_ID AS PersonID, 
        fcp.FACT_CP_PLAN_ID as CPEpisodeID, 
        TO_DATE(fcp.START_DTTM, 'yyyy-MM-dd HH:mm:ss') AS CPStartDate,
        TO_DATE(fcp.END_DTTM, 'yyyy-MM-dd HH:mm:ss') AS CPEndDate,
        CASE 
            WHEN fr.group_referral_id IS NULL THEN 
                concat_ws(
                '', 
                'CP', 
                CAST(fr.dim_person_id AS STRING), 
                date_format(to_timestamp(fcp.START_DTTM, 'yyyy-MM-dd HH:mm:ss'), 'yyyyMMdd')
                )
            ELSE 
                concat_ws(
                '', 
                'CP', 
                CAST(fr.group_referral_id AS STRING), 
                date_format(to_timestamp(fcp.START_DTTM, 'yyyy-MM-dd HH:mm:ss'), 'yyyyMMdd')
                )
        END AS GroupID
    FROM child_social.DIM_PERSON AS dp 
    JOIN child_social.FACT_CP_PLAN AS fcp ON dp.dim_person_id = fcp.dim_person_id 
    LEFT JOIN child_social.FACT_REFERRALS AS fr ON dp.LEGACY_ID = fr.dim_person_id 
    WHERE dp.LEGACY_ID <> 'Unknown'
""")

OverwriteLoad(
    df,
    'Tables/cdm/cp_episode',
    'cdm.cp_episode'
)


# In[8]:


df = spark.sql("""
    SELECT 
        dp.LEGACY_ID as PersonID, 
        dp.FORENAME as FirstName, 
        dp.SURNAME as Surname, 
        dp.BIRTH_DTTM as DOB, 
        dp.GENDER_DESCRIPTION as Gender 
    FROM child_social.DIM_PERSON dp
""")

OverwriteLoad(
    df,
    'Tables/cdm/intervention_person',
    'cdm.intervention_person'
)


# In[9]:


df = spark.sql("""
    SELECT 
        DIM_PERSON.UPN as UPN,
        DIM_PERSON.LEGACY_ID as SchoolPersonID,
        DIM_PERSON.FORENAME as FirstName,
        DIM_PERSON.SURNAME as Surname,
        DIM_PERSON.BIRTH_DTTM as DOB,
        DIM_PERSON.GENDER_DESCRIPTION as Gender 
    FROM child_social.DIM_PERSON
    WHERE DIM_PERSON.LEGACY_ID not like '%G_%' 
    AND DIM_PERSON.LEGACY_ID not like '%eStart%' 
    AND DIM_PERSON.UPN != 'Unknown'
""")

OverwriteLoad(
    df,
    'Tables/cdm/school_person',
    'cdm.school_person'
)


# In[11]:


df = spark.sql("""
    SELECT DISTINCT
        dp.SURNAME AS Surname,
        date_format(dp.BIRTH_DTTM, 'yyyy-MM-dd') AS DOB,
        dp.GENDER_DESCRIPTION AS Gender,
        dp.LEGACY_ID AS PersonID,
        dp.other_identifier_3 AS FamilyID,
        fce.FACT_CAF_EPISODE_ID AS EHEpisodeID,
        date_format(fce.EPISODE_START_DTTM, 'yyyy-MM-dd') AS EHStartDate,
        date_format(fce.EPISODE_END_DTTM, 'yyyy-MM-dd') AS EHEndDate,
        'REF' AS EHClosureReason,
        dp.other_identifier_3 AS GroupID
        FROM child_social.DIM_PERSON AS dp 
        JOIN child_social.FACT_CAF_EPISODE AS fce ON dp.dim_person_id = fce.dim_person_id 

""")

OverwriteLoad(
    df,
    'Tables/cdm/eh_episode',
    'cdm.eh_episode'
)


# In[12]:


df = spark.sql("""
    SELECT 
        dp.UPN as UPN, 
        dp.legacy_id as SchoolPersonID, 
        fsc.START_DTTM as ExclusionStartdate, 
        fsc.END_DTTM as ExclusionEndDate, 
        fsc.EXCLUSION_IN_DAYS as DaysExcluded, 
        fsc.DIM_LOOKUP_EXCLUSION_REASON_DESC as ExclusionEvent 
    FROM child_social.DIM_PERSON dp 
    INNER JOIN child_social.FACT_SCHOOL_EXCLUSION fsc ON dp.dim_person_id = fsc.dim_person_id
""")

OverwriteLoad(
    df,
    'Tables/cdm/exclusion_event',
    'cdm.exclusion_event'
)


# In[13]:


df = spark.sql("""
    WITH _allEvents AS (
  
    /* Get the first EH event that is within the last 2 years to use as the SF event. 
            Subsequent events may be counted as regression if within 6 months of close.
            Return only events that closed over 6 months ago as newer ones cannot yet be claimed*/
        SELECT 
            PersonID, 
            GroupID, 
            FamilyID, 
            EHStartDate AS SFStartDate, 
            EHEndDate AS SFEndDate, 
            'EH' AS Service, 
            EHClosureReason AS SFClosureReason, 
            ROW_NUMBER() OVER (
            PARTITION BY PersonID 
            ORDER BY 
                EHStartDate ASC
            ) AS rownum 
        FROM 
            cdm.EHEpisode
        WHERE 
        EHEndDate > add_months(current_date(), -12 * 5)
        AND EHEndDate < add_months(current_date(), -6)
        ) 
    SELECT 
    PersonID, 
    GroupID, 
    FamilyID, 
    SFStartDate, 
    SFEndDate, 
    Service, 
    SFClosureReason 
    FROM 
    _allEvents 
    WHERE 
    rownum = 1
""")

OverwriteLoad(
    df,
    'Tables/cdm/supporting_families_event',
    'cdm.supporting_families_event'
)


# In[14]:


df = spark.sql("""
    SELECT 
        dp.legacy_id as PersonID, 
        dp.UPN as UPN, 
        dp.other_identifier_3 as FamilyID, 
        fce.GROUP_EPISODE_ID as GroupID, 
        dp.forename as FirstName, 
        dp.surname as Surname, 
        dp.birth_dttm as DOB, 
        dp.GENDER_DESCRIPTION as Gender 
    FROM child_social.DIM_PERSON dp 
    INNER JOIN child_social.FACT_CAF_EPISODE fce ON dp.dim_person_id = fce.dim_person_id
""")

OverwriteLoad(
    df,
    'Tables/cdm/supporting_families_person',
    'cdm.supporting_families_person'
)


# In[15]:


df = spark.sql("""
WITH base AS (
  SELECT
    f.dim_person_id,
    p.dim_person_upn,

    -- Parse to DATE (works for timestamp or 'yyyy-MM-dd' strings)
    to_date(f.attendance_dttm) AS attendance_date,

    f.actual_attendance,
    f.possible_attendance,
    f.absence
  FROM education.FACT_CLIENT_ATTENDANCE f
  LEFT JOIN education.FACT_CLIENT_ATTENDANCE_SUMMARY p
    ON f.dim_person_id = p.dim_person_id
  WHERE f.attendance_dttm IS NOT NULL
),
tagged AS (
  SELECT
    dim_person_id,
    dim_person_upn,

    -- Academic year: Sep–Aug
    CASE
      WHEN month(attendance_date) >= 9 THEN year(attendance_date)
      ELSE year(attendance_date) - 1
    END AS `year`,

    -- Term by month
    CASE
      WHEN month(attendance_date) BETWEEN 9 AND 12 THEN 1
      WHEN month(attendance_date) BETWEEN 1 AND 4  THEN 2
      WHEN month(attendance_date) BETWEEN 5 AND 8  THEN 3
      ELSE NULL
    END AS term,

    actual_attendance,
    possible_attendance,
    absence
  FROM base
)
SELECT
  dim_person_id,
  dim_person_upn,
  `year`,
  term,
  SUM(actual_attendance)   AS termlysessionsauthorised,
  SUM(possible_attendance) AS termlysessionspossible,
  SUM(absence)             AS termlysessionsunauthorised
FROM tagged
GROUP BY
  dim_person_id,
  dim_person_upn,
  `year`,
  term
""")

OverwriteLoad(
    df,
    'Tables/cdm/pupil_on_roll',
    'cdm.pupil_on_roll'
)


# In[16]:


df = spark.sql("""
    SELECT 
        p.dim_person_upn AS UPN, 
        p.dim_person_id AS SchoolPersonID, 
        p.year AS Year, 
        p.term AS Term, 
        p.termlysessionspossible AS AvailableSessions, 
        p.termlysessionsauthorised AS AuthorisedSessions, 
        p.termlysessionsunauthorised AS UnauthorisedSessions 
    FROM cdm.pupil_on_roll AS p 
    WHERE 
    p.year IN ('2023', '2024','2025')
""")

OverwriteLoad(
    df,
    'Tables/cdm/school_event',
    'cdm.school_event'
)


# In[17]:


df = spark.sql("""
SELECT
  UPN,
  SchoolPersonID,
  Year,
  Term,
  AvailableSessions,
  AuthorisedSessions,
  UnauthorisedSessions,
  CONCAT(
    CAST(CAST(Year AS INT) AS STRING),
    CAST(CAST(Year AS INT) + 1 AS STRING),
    '0',
    CAST(Term AS STRING)
  ) AS TermKey
FROM cdm.school_event
""")

OverwriteLoad(
    df,
    'Tables/cdm/vw_school_event',
    'cdm.vw_school_event'
)


# In[18]:


df = spark.sql("""
CREATE OR REPLACE TABLE
cdm.school_term_dates
AS
SELECT 

 col1 AS Year,
 col2 AS   Term,
 to_date(col3, 'dd/MM/yyyy') AS   TermStartDate,
 to_date(col4, 'dd/MM/yyyy') AS  TermEndDate

FROM VALUES
('2015/16',	1, '01/09/2015',  '31/12/2015'),
('2015/16',	2, 	'01/01/2016',  	'30/04/2016'),
('2015/16',	3, '01/05/2016',   	'31/08/2016'),
('2016/17',	1, 	'01/09/2016',  	'31/12/2016'),
('2016/17',	2, 	'01/01/2017',  	'30/04/2017'),
('2016/17',	3, 	'01/05/2017',  	'31/08/2017'),
('2017/18',	1, 	'01/09/2017',  	'31/12/2017'),
('2017/18',	2, 	'01/01/2018',  	'30/04/2018'),
('2017/18',	3, 	'01/05/2018',  	'31/08/2018'),
('2018/19',	1, 	'01/09/2018',  	'31/12/2018'),
('2018/19',	2, 	'01/01/2019',  	'30/04/2019'),
('2018/19',	3, 	'01/05/2019',  	'31/08/2019'),
('2019/20',	1, 	'01/09/2019',  	'31/12/2019'),
('2019/20',	2, 	'01/01/2020',  	'30/04/2020'),
('2019/20',	3, 	'01/05/2020',  	'31/08/2020'),
('2020/21',	1, 	'01/09/2020',  	'31/12/2020'),
('2020/21',	2, 	'01/01/2021',  	'30/04/2021'),
('2020/21',	3, 	'01/05/2021',  	'31/08/2021'),
('2021/22',	1, 	'01/09/2021',  	'31/12/2021'),
('2021/22',	2, 	'01/01/2022',  	'30/04/2022'),
('2021/22',	3, 	'01/05/2022',  	'31/08/2022'),
('2022/23',	1, 	'01/09/2022',  	'31/12/2022'),
('2022/23',	2, 	'01/01/2023',  	'30/04/2023'),
('2022/23',	3, 	'01/05/2023',  	'31/08/2023'),
('2023/24',	1, 	'01/09/2023',  	'31/12/2023'),
('2023/24',	2, 	'01/01/2024',  	'30/04/2024'),
('2023/24',	3, 	'01/05/2024',  	'31/08/2024'),
('2024/25',	1, 	'01/09/2024',  	'31/12/2024'),
('2024/25',	2, 	'01/01/2025',  	'30/04/2025'),
('2024/25',	3, 	'01/05/2025',  	'31/08/2025'),
('2025/26',	1, 	'01/09/2025',  	'31/12/2025'),
('2025/26', 2,  '01/01/2026',   '30/04/2026'),
('2025/26', 3,  '01/05/2026',   '31/08/2026'),
('2026/27', 1,  '01/09/2026',   '31/12/2026'),
('2026/27', 2,  '01/01/2027',   '30/04/2027'),
('2026/27', 3,  '01/05/2027',   '31/08/2027')
""")


# In[3]:


df = spark.sql("""
WITH terms_cte AS (
    SELECT
        ROW_NUMBER() OVER (ORDER BY TermStartDate DESC) AS RowNum,
        CASE
            WHEN current_date() BETWEEN TermStartDate AND TermEndDate THEN 1
            ELSE 0
        END AS IsCurrent,

        -- remove '/' (and anything non-digit), then build TermKey
        CONCAT(
            substring(regexp_replace(`Year`, '[^0-9]', ''), 1, 4), -- e.g. 2023
            substring(regexp_replace(`Year`, '[^0-9]', ''), 5, 2), -- e.g. 24
            '0',
            CAST(Term AS STRING)
        ) AS TermKey,

        `Year`,
        Term,
        TermStartDate,
        TermEndDate
    FROM cdm.school_term_dates
),
cur AS (
    SELECT MAX(CASE WHEN IsCurrent = 1 THEN RowNum END) AS CurrentRowNum
    FROM terms_cte
)
SELECT
    t.TermKey,
    t.`Year`,
    t.Term,
    t.TermStartDate,
    t.TermEndDate,
    COALESCE(c.CurrentRowNum, 0) - t.RowNum AS RelativeTerm
FROM terms_cte t
CROSS JOIN cur c
""")

OverwriteLoad(
    df,
    "Tables/cdm/vw_school_term_dates_old",
    "cdm.vw_school_term_dates_old"
)


# In[4]:


df = spark.sql("""
WITH terms_cte AS (
  SELECT
    ROW_NUMBER() OVER (ORDER BY TermStartDate DESC) AS RowNum,
    CASE WHEN current_date() BETWEEN TermStartDate AND TermEndDate THEN 1 ELSE 0 END AS IsCurrent,

    -- Turn '2023/24' into startYear=2023 and endYear=2024
    CAST(substring(regexp_replace(`Year`, '[^0-9]', ''), 1, 4) AS INT) AS StartYear,
    CAST(concat('20', substring(regexp_replace(`Year`, '[^0-9]', ''), 5, 2)) AS INT) AS EndYear,

    `Year`,
    Term,
    TermStartDate,
    TermEndDate
  FROM cdm.school_term_dates
),
terms_with_key AS (
  SELECT
    RowNum,
    IsCurrent,
    CONCAT(
      CAST(StartYear AS STRING),
      CAST(EndYear AS STRING),
      '0',
      CAST(Term AS STRING)
    ) AS TermKey,
    `Year`,
    Term,
    TermStartDate,
    TermEndDate
  FROM terms_cte
),
cur AS (
  SELECT MAX(CASE WHEN IsCurrent = 1 THEN RowNum END) AS CurrentRowNum
  FROM terms_with_key
)
SELECT
  t.TermKey,
  t.`Year`,
  t.Term,
  t.TermStartDate,
  t.TermEndDate,
  COALESCE(c.CurrentRowNum, 0) - t.RowNum AS RelativeTerm
FROM terms_with_key t
CROSS JOIN cur c
""")

OverwriteLoad(
    df,
    "Tables/cdm/vw_school_term_dates",
    "cdm.vw_school_term_dates"
)


# In[20]:


df = spark.sql("""
SELECT 
    exclusion.*, 
    term.TermKey
FROM cdm.exclusion_event AS exclusion
JOIN cdm.vw_school_term_dates AS term 
    ON term.TermStartDate <= exclusion.ExclusionStartdate AND term.TermEndDate > exclusion.ExclusionStartdate;
""")

OverwriteLoad(
    df,
    'Tables/cdm/vw_exclusion_event',
    'cdm.vw_exclusion_event'
)


# In[10]:


df = spark.sql("""
SELECT 
    person.UPN,
    person.SchoolPersonID, 
    startTerm.RelativeTerm AS RelativeStartTerm,
    startTerm.TermKey AS StartTermKey,
    endTerm.RelativeTerm AS RelativeEndTerm,
    endTerm.TermKey AS EndTermKey
FROM cdm.school_person AS person 
JOIN cdm.supporting_families_person AS sfPerson ON sfPerson.PersonID = person.SchoolPersonID
JOIN cdm.supporting_families_event AS sfEvent ON sfEvent.PersonID = sfPerson.PersonID
JOIN cdm.vw_school_term_dates AS startTerm ON startTerm.TermStartDate <= sfEvent.SFStartDate AND startTerm.TermEndDate > sfEvent.SFStartDate
JOIN cdm.vw_school_term_dates AS endTerm ON endTerm.TermStartDate < sfEvent.SFEndDate AND endTerm.TermEndDate >= sfEvent.SFEndDate;
  
""")

OverwriteLoad(
    df,
    'Tables/cdm/vw_relative_term_dates',
    'cdm.vw_relative_term_dates'
)


# In[22]:


df = spark.sql("""
WITH _exclusions AS
(
    /*  Create a bulk table for every child for every term.
        SUM the number of exclusions for each child for each term. 
        Where there is no record in ExclusionEvent, the number of exclusions for that child for that term is 0 */
    SELECT 	
        allExc.UPN, 
        allExc.SchoolPersonID, 
        allExc.GroupID,
        allExc.TermKey,
        allExc.RelativeTerm,
        --SUM(ISNULL(exclusions.DaysExcluded,0)) AS DaysExcluded    
        SUM(COALESCE(exclusions.DaysExcluded,0)) AS DaysExcluded  
    FROM cdm.vw_exclusion_event AS exclusions
    RIGHT JOIN 
        (
            SELECT 
                terms.TermKey, terms.RelativeTerm, 
                person.UPN, person.SchoolPersonID, sfEvent.GroupID
            FROM cdm.school_person AS person 
            JOIN cdm.supporting_families_person AS sfPerson ON sfPerson.PersonID = person.SchoolPersonID
            JOIN cdm.supporting_families_event AS sfEvent ON sfEvent.PersonID = sfPerson.PersonID
            FULL OUTER JOIN cdm.vw_school_term_dates AS terms ON 1=1
            JOIN cdm.vw_relative_term_dates AS startTerm ON startTerm.SchoolPersonID = person.SchoolPersonID
            JOIN cdm.vw_relative_term_dates AS endTerm ON endTerm.SchoolPersonID = person.SchoolPersonID
            /* 0 is current term, get all data up to the end of the last complete term from 2 complete terms preceding the start term*/
            WHERE terms.RelativeTerm BETWEEN startTerm.RelativeStartTerm-3 AND -1 
        ) allExc
        ON allExc.SchoolPersonID = exclusions.SchoolPersonID AND allExc.TermKey = exclusions.TermKey 
    GROUP BY 
        allExc.UPN, 
        allExc.SchoolPersonID, 
        allExc.GroupID,
        allExc.TermKey,
        allExc.RelativeTerm
),
_rankedExclusions AS
(
    /* Sum all the exclusions for each child across each two terms (e.g. term 1 and term 2, term 2 and term 3)
    And Rank them to find the two terms that give the highest number. This is the high point to compare to*/
    SELECT *,
    RANK() OVER (PARTITION BY SchoolPersonID ORDER BY TwoMonthTotal DESC, RelativeTerm DESC) AS MostExclusions
    FROM (
        SELECT exclusions.*, 
        SUM(DaysExcluded) OVER(PARTITION BY exclusions.SchoolPersonID ORDER BY exclusions.RelativeTerm ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) AS TwoMonthTotal
        FROM _exclusions AS exclusions
        JOIN cdm.vw_relative_term_dates AS endTerm ON exclusions.SchoolPersonID = endTerm.SchoolPersonID
        /* only rank terms up to the end of the supporting families intervention */
        WHERE RelativeTerm <= endTerm.RelativeEndTerm
        ) r
)
SELECT DISTINCT
    excl.UPN,
    excl.SchoolPersonID, excl.GroupID,
    CAST(topExclusions.TwoMonthTotal / 2 AS DECIMAL(4,1)) AS HighestAverageOverTwoTerms,
    previousTermExclusions.DaysExcluded AS DaysExcludedLastTerm,
    previousPreviousTermExclusions.DaysExcluded AS DaysExcludedTermBeforeLast
FROM _exclusions AS excl
JOIN     
    (
        /* The highest number of exclusions from the ranked data)*/
        SELECT UPN, SchoolPersonID, TwoMonthTotal
        FROM _rankedExclusions WHERE MostExclusions = 1
    ) AS topExclusions 
    ON topExclusions.UPN = excl.UPN
JOIN
    (
        /* Last term's exclusions*/
        SELECT UPN, SchoolPersonID,  
        SUM(DaysExcluded) AS DaysExcluded
        FROM _exclusions WHERE RelativeTerm = -1
        GROUP BY UPN, SchoolPersonID 
    ) AS previousTermExclusions
    ON previousTermExclusions.UPN = excl.UPN
JOIN
    (
        /* The term before last term's exclusions*/
        SELECT UPN, SchoolPersonID,  
        SUM(DaysExcluded) AS DaysExcluded
        FROM _exclusions WHERE RelativeTerm = -2
        GROUP BY UPN, SchoolPersonID 
    ) AS previousPreviousTermExclusions
    ON previousPreviousTermExclusions.UPN = excl.UPN;
""")

OverwriteLoad(
    df,
    'Tables/cdm/education_exclusions',
    'cdm.education_exclusions'
)



# In[23]:


df = spark.sql("""
SELECT
  sfPerson.*,
  CAST(floor(months_between(sfEvent.SFStartDate, sfPerson.DOB) / 12) AS INT) AS AgeAtSFStartDate,
  CAST(floor(months_between(sfEvent.SFEndDate,   sfPerson.DOB) / 12) AS INT) AS AgeAtSFEndDate
FROM cdm.SupportingFamiliesPerson AS sfPerson
JOIN cdm.SupportingFamiliesEvent  AS sfEvent
  ON sfEvent.PersonID = sfPerson.PersonID
""")

OverwriteLoad(
    df,
    'Tables/cdm/vw_supporting_families_person',
    'cdm.vw_supporting_families_person'
)


# In[25]:


df = spark.sql("""
SELECT 
    sfEvent.PersonID, 
	sfEvent.FamilyID as FamilyID,
	sfEvent.GroupID  AS SFGroupID, 
    sfEvent.SFStartDate, sfEvent.SFEndDate,
    regressions.RegressionGroupID, regressions.RegressionType, regressions.EpisodeID, 
    regressions.EpisodeStart, regressions.EpisodeEnd
FROM cdm.supporting_families_event AS sfEvent
LEFT OUTER JOIN
(
SELECT 
    firstep.PersonID, firstep.RegressionGroupID,
    firstep.RegressionType, firstep.EpisodeID, firstep.EpisodeStart, firstep.EpisodeEnd
FROM 
    (
        SELECT 
            ep.PersonID, ep.GroupID AS RegressionGroupID, ep.EpisodeType AS RegressionType, EpisodeID, EpisodeStart, EpisodeEnd
            FROM
            (
                SELECT allepisodes.PersonID, allepisodes.GroupID, allepisodes.EpisodeType, allepisodes.EpisodeID, allepisodes.EpisodeStart, allepisodes.EpisodeEnd,
                ROW_NUMBER() OVER (PARTITION BY allepisodes.PersonID ORDER BY EpisodeStart ASC) AS rownum
                FROM 
                (
                    SELECT eh.PersonID, eh.GroupID, 'EH' AS EpisodeType, eh.EHEpisodeID AS EpisodeID, eh.EHStartDate AS EpisodeStart, eh.EHEndDate AS EpisodeEnd
                    FROM cdm.EHEpisode AS eh 
                    UNION ALL
                    SELECT cin.PersonID, cin.GroupID, 'CIN' AS EpisodeType, cin.CINEpisodeID AS EpisodeID, cin.CINStartDate AS EpisodeStart, cin.CINEndDate AS EpisodeEnd
                    FROM cdm.CINEpisode AS cin 
                   -- UNION ALL
                   --SELECT cp.PersonID, cp.GroupID, 'CP' AS EpisodeType, cp.CPEpisodeID AS EpisodeID, cp.CPStartDate AS EpisodeStart, cp.CPEndDate AS EpisodeEnd
                   -- FROM cdm.CPEpisode AS cp 
                   --UNION ALL
                   -- SELECT cla.PersonID, cla.GroupID, 'CLA' AS EpisodeType, cla.CLAEpisodeID AS EpisodeID, cla.CLAStartDate AS EpisodeStart, cla.CLAEndDate AS EpisodeEnd
                   -- FROM cdm.CLAEpisode AS cla 
                ) allepisodes
                JOIN cdm.supporting_families_event AS sfEvent ON sfEvent.PersonID = allepisodes.PersonID
                WHERE DATEDIFF(day, allepisodes.EpisodeStart, sfEvent.SFEndDate) < 0 AND DATEDIFF(day, allepisodes.EpisodeStart, DATEADD(month,6,sfEvent.SFEndDate)) > 0 
            ) ep
        WHERE rownum = 1
    ) firstep
) AS regressions ON regressions.PersonID = sfEvent.PersonID;
""")

OverwriteLoad(
    df,
    'Tables/cdm/keeping_children_safe_social_care',
    'cdm.keeping_children_safe_social_care'
)


# In[26]:


df = spark.sql("""
SELECT 
    sfPerson.PersonID, 
	sfEvent.FamilyID,
    sfEvent.GroupID,
    sfEvent.SFStartDate,
    sfEvent.SFEndDate,
    CASE WHEN 
        SUM(CASE WHEN 
                mfh.MfHEndDate > DATEADD(month, -12, sfEvent.SFStartDate) AND mfh.MfHEndDate <= sfEvent.SFStartDate
            THEN 1 ELSE 0 END) >= 1 
        THEN 1 ELSE 0 END 
        AS NeedIdentified,
    CASE WHEN 
        SUM(CASE WHEN 
                mfh.MfHEndDate BETWEEN DATEADD(month, -1, sfEvent.SFEndDate) AND sfEvent.SFEndDate
            THEN 1 ELSE 0 END) >= 1 
        THEN 1 ELSE 0 END 
        AS MfHMonth1BeforeClose,
    CASE WHEN 
        SUM(CASE WHEN 
                mfh.MfHStartDate > sfEvent.SFEndDate AND mfh.MfHStartDate <= DATEADD(month, 6, sfEvent.SFEndDate)
            THEN 1 ELSE 0 END) >= 1 
        THEN 1 ELSE 0 END 
        AS MfHMonth6AfterClose
FROM cdm.mfh_episode AS mfh
RIGHT JOIN cdm.supporting_families_person AS sfPerson ON sfPerson.PersonID = mfh.PersonID
JOIN cdm.supporting_families_event AS sfEvent ON sfEvent.PersonID = sfPerson.PersonID
GROUP BY sfPerson.PersonID, sfEvent.FamilyID, sfEvent.GroupID, sfEvent.SFStartDate,
    sfEvent.SFEndDate;
""")

OverwriteLoad(
    df,
    'Tables/cdm/keeping_children_safe_missing_from_home',
    'cdm.keeping_children_safe_missing_from_home'
)


# In[11]:


df = spark.sql("""
SELECT DISTINCT
    allTerms.UPN,
    allTerms.SchoolPersonID,
    allTerms.FamilyID,
    allTerms.GroupID,
    allTerms.TermKey,
    schoolEvent.AvailableSessions,
    schoolEvent.AuthorisedSessions,
    schoolEvent.UnauthorisedSessions,
    allTerms.RelativeTerm,
    allTerms.RelativeStartTerm,
    allTerms.RelativeEndTerm,
    allTerms.SFStartDate,
    allTerms.SFEndDate
FROM cdm.vw_school_event AS schoolEvent
JOIN (
    SELECT
        terms.TermKey,
        terms.RelativeTerm,
        startTerm.RelativeStartTerm,
        endTerm.RelativeEndTerm,
        person.UPN,
        person.SchoolPersonID,
        sfEvent.FamilyID,
        sfEvent.GroupID,
        sfEvent.SFStartDate,
        sfEvent.SFEndDate
    FROM cdm.school_person AS person
    JOIN cdm.supporting_families_person AS sfPerson
      ON upper(trim(sfPerson.UPN)) = upper(trim(person.UPN))
    JOIN cdm.supporting_families_event AS sfEvent
      ON sfEvent.PersonID = sfPerson.PersonID
    JOIN cdm.vw_school_term_dates AS terms
      ON 1 = 1
    JOIN cdm.vw_relative_term_dates AS startTerm
      ON startTerm.SchoolPersonID = person.SchoolPersonID
    JOIN cdm.vw_relative_term_dates AS endTerm
      ON endTerm.SchoolPersonID = person.SchoolPersonID
    WHERE terms.RelativeTerm >= startTerm.RelativeStartTerm - 3
) allTerms
ON upper(trim(allTerms.UPN)) = upper(trim(schoolEvent.UPN))
AND CAST(allTerms.TermKey AS STRING) = CAST(schoolEvent.TermKey AS STRING)
""")

OverwriteLoad(
    df,
    'Tables/cdm/vw_attendance',
    'cdm.vw_attendance'
)


# In[3]:


df = spark.sql("""
SELECT DISTINCT
    allTerms.UPN,
    allTerms.SchoolPersonID,
    allTerms.FamilyID,
	allTerms.GroupID,
    ----schoolEvent.SchoolID,
    allTerms.TermKey,
    schoolEvent.AvailableSessions,
    schoolEvent.AuthorisedSessions,
    schoolEvent.UnauthorisedSessions,
    allTerms.RelativeTerm,
    allTerms.RelativeStartTerm,
    allTerms.RelativeEndTerm,
    allTerms.SFStartDate,
    allTerms.SFEndDate
FROM cdm.vw_school_event AS schoolEvent
JOIN (
    SELECT
        terms.TermKey,
        terms.RelativeTerm,
        startTerm.RelativeStartTerm,
        endTerm.RelativeEndTerm,
        person.UPN,
        person.SchoolPersonID,
		sfEvent.FamilyID,
        sfEvent.GroupID,
        sfEvent.SFStartDate,
        sfEvent.SFEndDate
    FROM cdm.school_person AS person
    JOIN cdm.supporting_families_person AS sfPerson ON sfPerson.UPN = person.UPN
    JOIN cdm.supporting_families_event AS sfEvent ON sfEvent.PersonID = sfPerson.PersonID
    FULL OUTER JOIN cdm.vw_school_term_dates AS terms ON 1=1
    JOIN cdm.vw_relative_term_dates AS startTerm ON startTerm.SchoolPersonID = person.SchoolPersonID
    JOIN cdm.vw_relative_term_dates AS endTerm ON endTerm.SchoolPersonID = person.SchoolPersonID
    WHERE terms.RelativeTerm >= startTerm.RelativeStartTerm - 3
) allTerms
ON allTerms.UPN = schoolEvent.UPN AND allTerms.TermKey = schoolEvent.TermKey;
""")

OverwriteLoad(
    df,
    'Tables/cdm/vw_attendance_old',
    'cdm.vw_attendance_old'
)


# In[20]:


df = spark.sql("""
SELECT
FamilyID,
GroupID,
SchoolPersonId,
Attendance_1_Need,
Attendance_1_Need_Met_Individual,
Attendance_2_Need,
Attendance_2_Need_Met,
Attendance_2_Need_Met_Individual
FROM cdm.education_attendance_needsmet_calcs
ORDER BY FamilyID
""")

OverwriteLoad(
    df,
    'Tables/cdm/education_attendance_needsmet_summary_detail',
    'cdm.education_attendance_needsmet_summary_detail'
)


# In[18]:


df = spark.sql("""
WITH Calc AS (
  SELECT
    ea.*,

    -- Calculate Average Over Last 2 Terms (Auth Absence)
    (
      (ea.CloseTermAvailableSessions + ea.NextTermAvailableSessions)
    - (ea.CloseTermUnauthorisedSessions + ea.NextTermUnauthorisedSessions)
    - (ea.CloseTermAuthorisedSessions + ea.NextTermAuthorisedSessions)
    ) * 1.0
    / CASE
        WHEN (ea.CloseTermAvailableSessions + ea.NextTermAvailableSessions) = 0
        THEN NULL
        ELSE (ea.CloseTermAvailableSessions + ea.NextTermAvailableSessions)
      END
    AS Avg_Over_Last2_Terms_Auth_Absence,

    -- Calculate Average Over Last 2 terms (Unauth absence)
    (
      (ea.CloseTermAvailableSessions + ea.NextTermAvailableSessions)
    - (ea.CloseTermUnauthorisedSessions + ea.NextTermUnauthorisedSessions)
    ) * 1.0
    / CASE
        WHEN (ea.CloseTermAvailableSessions + ea.NextTermAvailableSessions) = 0
        THEN NULL
        ELSE (ea.CloseTermAvailableSessions + ea.NextTermAvailableSessions)
      END
    AS Avg_Over_Last2_Terms_Unauth_Absence

  FROM cdm.education_attendance ea
),

Calc2 AS (
  SELECT
    ea.*,

    -- Calculate Average Over Last 2 Terms (Incl Authorised if lowest attendance < 50%)
    CASE
      WHEN ea.LowestAttendanceAuthPercent < 0.5
        THEN ea.Avg_Over_Last2_Terms_Auth_Absence
      ELSE ea.Avg_Over_Last2_Terms_Unauth_Absence
    END AS Avg_Over_Last2_Terms_Incl_Authorised

  FROM Calc ea
),

Calc3 AS (
  SELECT
    c2.*,

    -- Calculate Percentage Increase
    (c2.Avg_Over_Last2_Terms_Incl_Authorised - c2.LowestAttendanceAuthPercent) * 1.0
    / CASE
        WHEN c2.LowestAttendanceAuthPercent = 0
        THEN NULL
        ELSE c2.LowestAttendanceAuthPercent
      END
    AS PercentageIncrease

  FROM Calc2 c2
)

SELECT
  ea.*,

  CASE
    WHEN ea.LowestAttendanceUnauthPercent < 0.9 THEN 'Yes'
    ELSE 'No'
  END AS `Attendance_1_Need`,

  CASE
    WHEN ea.Avg_Over_Last2_Terms_Incl_Authorised > 0.9 THEN 'Yes'
    ELSE 'No'
  END AS `Attendance_1_Need_Met_Individual`,

  CASE
    WHEN ea.LowestAttendanceAuthPercent < 0.5 THEN 'Yes'
    ELSE 'No'
  END AS `Attendance_2_Need`,

  CASE
    WHEN ea.LowestAttendanceAuthPercent < 0.5
      THEN CASE WHEN ea.PercentageIncrease > 0.3 THEN 1 ELSE -1 END
    ELSE 100
  END AS `Attendance_2_Need_Met`,

  CASE
    WHEN (
      CASE
        WHEN ea.LowestAttendanceAuthPercent < 0.5
          THEN CASE WHEN ea.PercentageIncrease > 0.3 THEN 1 ELSE -1 END
        ELSE 100
      END
    ) = -1 THEN 'No'
    WHEN (
      CASE
        WHEN ea.LowestAttendanceAuthPercent < 0.5
          THEN CASE WHEN ea.PercentageIncrease > 0.3 THEN 1 ELSE -1 END
        ELSE 100
      END
    ) = 1 THEN 'Yes'
    ELSE 'N/A'
  END AS `Attendance_2_Need_Met_Individual`

FROM Calc3 ea;
""")

OverwriteLoad(
    df,
    'Tables/cdm/education_attendance_needsmet_calcs',
    'cdm.education_attendance_needsmet_calcs'
)


# In[12]:


df = spark.sql("""
 SELECT
    *,
    RANK() OVER (PARTITION BY SchoolPersonID ORDER BY AttendanceOverTwoMonthsUnauth ASC) AS RankedUnauthorisedAbsense,
    RANK() OVER (PARTITION BY SchoolPersonID ORDER BY AttendanceOverTwoMonthsAuth ASC) AS RankedAuthorisedUnauthorisedAbsense
FROM (
    SELECT
        sumEvent.*,
        (CASE
            WHEN sumEvent.TotalAvailableOver2Months != 0 THEN
                (CAST(sumEvent.TotalAvailableOver2Months AS decimal(10,2)) - CAST(sumEvent.TotalUnauthOver2Months AS DECIMAL(10,2)))
                / NULLIF(CAST(sumEvent.TotalAvailableOver2Months AS DECIMAL(10,2)),0)
            ELSE NULL
        END) AS AttendanceOverTwoMonthsUnauth,
        (CASE
            WHEN sumEvent.TotalAvailableOver2Months != 0 THEN
                (CAST(sumEvent.TotalAvailableOver2Months AS decimal(10,2)) - CAST(sumEvent.TotalUnauthOver2Months AS DECIMAL(10,2)) - CAST(sumEvent.TotalAuthOver2Months AS DECIMAL(10,2)))
                / NULLIF(CAST(sumEvent.TotalAvailableOver2Months AS DECIMAL(10,2)),0)
            ELSE NULL
        END) AS AttendanceOverTwoMonthsAuth
    FROM (
        SELECT
            attendance.*,
            SUM(UnauthorisedSessions) OVER (PARTITION BY attendance.SchoolPersonID ORDER BY RelativeTerm ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) AS TotalUnauthOver2Months,
            SUM(AuthorisedSessions) OVER (PARTITION BY attendance.SchoolPersonID ORDER BY RelativeTerm ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) AS TotalAuthOver2Months,
            SUM(AvailableSessions) OVER (PARTITION BY attendance.SchoolPersonID ORDER BY RelativeTerm ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) AS TotalAvailableOver2Months,
            MIN(RelativeTerm) OVER (PARTITION BY attendance.SchoolPersonID) AS FirstTerm
        FROM cdm.vw_attendance AS attendance
        JOIN cdm.vw_relative_term_dates AS endTerm ON attendance.SchoolPersonID = endTerm.SchoolPersonID
       ---WHERE attendance.RelativeTerm < endTerm.RelativeEndTerm
	   WHERE attendance.RelativeTerm > endTerm.RelativeEndTerm
    ) sumEvent
) r   
""")

OverwriteLoad(
    df,
    'Tables/cdm/vw_ranked_attendance',
    'cdm.vw_ranked_attendance'
)


# In[14]:


df = spark.sql("""
SELECT
  DISTINCT
    att.UPN,
    att.SchoolPersonID,
	att.FamilyID,
    att.GroupID,
    att.SFStartDate,
    att.SFEndDate,
    unauthorisedAbsence.TermKey AS LowestUnauthTermKey,
    unauthorisedAbsence.TotalAvailableOver2Months AS LowestUnauthTermsTotalAvailable,
    unauthorisedAbsence.TotalUnauthOver2Months AS LowestUnauthTermsTotalUnauthAbsense,
    unauthorisedAbsence.TotalAuthOver2Months AS LowestUnauthTermsTotalAuthAbsense,
    unauthorisedAbsence.AttendanceOverTwoMonthsUnauth AS LowestAttendanceUnauthPercent,
    authorisedAbsence.TermKey AS LowestAuthTermKey,
    authorisedAbsence.TotalAvailableOver2Months AS LowestAuthTermsTotalAvailable,
    authorisedAbsence.TotalUnauthOver2Months AS LowestAuthTermsTotalUnauthAbsense,
    authorisedAbsence.TotalAuthOver2Months AS LowestAuthTermsTotalAuthAbsense,
    authorisedAbsence.AttendanceOverTwoMonthsAuth AS LowestAttendanceAuthPercent,
    closeTerm.TermKey AS CloseTerm,
    closeTerm.AvailableSessions AS CloseTermAvailableSessions,
    closeTerm.UnauthorisedSessions AS CloseTermUnauthorisedSessions,
    closeTerm.AuthorisedSessions AS CloseTermAuthorisedSessions,
    closeTerm.CloseTermAttendanceUnauthPercent,
    closeTerm.CloseTermAttendanceAuthAndUnauthPercent,
    nextTerm.TermKey AS NextTerm,
    nextTerm.AvailableSessions AS NextTermAvailableSessions,
    nextTerm.UnauthorisedSessions AS NextTermUnauthorisedSessions,
    nextTerm.AuthorisedSessions AS NextTermAuthorisedSessions,
    nextTerm.NextTermAttendanceUnauthPercent,
    nextTerm.NextTermAttendanceAuthAndUnauthPercent
FROM cdm.vw_ranked_attendance AS att
JOIN (
    SELECT UPN, TermKey,
    TotalAvailableOver2Months, TotalUnauthOver2Months, TotalAuthOver2Months, AttendanceOverTwoMonthsUnauth
    FROM cdm.vw_ranked_attendance WHERE RankedUnauthorisedAbsense = 1
) AS unauthorisedAbsence
ON unauthorisedAbsence.UPN = att.UPN
JOIN (
    SELECT UPN, TermKey,
    TotalAvailableOver2Months, TotalUnauthOver2Months, TotalAuthOver2Months, AttendanceOverTwoMonthsAuth
    FROM cdm.vw_ranked_attendance WHERE RankedAuthorisedUnauthorisedAbsense = 1
) AS authorisedAbsence
ON authorisedAbsence.UPN = att.UPN
JOIN (
    SELECT UPN, TermKey,
    AvailableSessions, UnauthorisedSessions, AuthorisedSessions,
    (CASE
        WHEN AvailableSessions != 0 THEN
            (CAST(AvailableSessions AS DECIMAL(10,2)) - CAST(UnauthorisedSessions AS DECIMAL(10,2)))
            / CAST(AvailableSessions AS DECIMAL(10,2))
        ELSE NULL
    END) AS CloseTermAttendanceUnauthPercent,
    (CASE
        WHEN AvailableSessions != 0 THEN
            (CAST(AvailableSessions AS DECIMAL(10,2)) - CAST(UnauthorisedSessions AS DECIMAL(10,2)) - CAST(AuthorisedSessions AS DECIMAL(10,2)))
            / CAST(AvailableSessions AS DECIMAL(10,2))
        ELSE NULL
    END) AS CloseTermAttendanceAuthAndUnauthPercent
    FROM cdm.vw_attendance
    --WHERE RelativeTerm = RelativeEndTerm
) AS closeTerm
ON closeTerm.UPN = att.UPN
JOIN (
    SELECT UPN, TermKey,
    AvailableSessions, UnauthorisedSessions, AuthorisedSessions,
    (CASE
        WHEN AvailableSessions != 0 THEN
            (CAST(AvailableSessions AS DECIMAL(10,2)) - CAST(UnauthorisedSessions AS DECIMAL(10,2)))
            / CAST(AvailableSessions AS DECIMAL(10,2))
        ELSE NULL
    END) AS NextTermAttendanceUnauthPercent,
    (CASE
        WHEN AvailableSessions != 0 THEN
            (CAST(AvailableSessions AS DECIMAL(10,2)) - CAST(UnauthorisedSessions AS DECIMAL(10,2)) - CAST(AuthorisedSessions AS DECIMAL(10,2)))
            / CAST(AvailableSessions AS DECIMAL(10,2))
        ELSE NULL
    END) AS NextTermAttendanceAuthAndUnauthPercent
    FROM cdm.vw_attendance
    --WHERE RelativeTerm = RelativeEndTerm + 1
) AS nextTerm
ON nextTerm.UPN = att.UPN;
""")

OverwriteLoad(
    df,
    'Tables/cdm/education_attendance_calculations',
    'cdm.education_attendance_calculations'
)


# In[21]:


df = spark.sql("""
WITH WithNeedMet AS (
    SELECT *,
        CASE
            WHEN EpisodeID IS NULL THEN 1
            ELSE -1
        END AS NeedMet
    FROM cdm.KeepingChildrenSafe_SocialCare
),

GroupMin AS (
    SELECT
        FamilyID,
        MIN(NeedMet) AS MinNeedMetInGroup
    FROM WithNeedMet
    GROUP BY FamilyID
)

SELECT
    EA.FamilyID,
    EA.SchoolPersonID,

    -- Attendance 1 Need Status
    CASE
       WHEN EA.Attendance_1_Need = 'Yes' THEN 'Pass'
       WHEN EA.Attendance_1_Need = 'No' THEN 'Fail'
       ELSE NULL
    END AS Attendance1NeedStatus,

    -- Attendance 1 Need Met Individual Status
    CASE
       WHEN EA.Attendance_1_Need_Met_Individual = 'Yes' THEN 'Pass'
       WHEN EA.Attendance_1_Need_Met_Individual = 'No' THEN 'Fail'
       ELSE NULL
    END AS Attendance1NeedMetIndividualStatus,

    -- Attendance 2 Need Status
    CASE
       WHEN EA.Attendance_2_Need = 'Yes' THEN 'Pass'
       WHEN EA.Attendance_2_Need = 'No' THEN 'Fail'
       ELSE NULL
    END AS Attendance2NeedStatus,

    -- Attendance 2 Need Met Individual Status
    CASE
       WHEN EA.Attendance_2_Need_Met_Individual = 'Yes' THEN 'Pass'
       WHEN EA.Attendance_2_Need_Met_Individual = 'No' THEN 'Fail'
       ELSE 'N/A'
    END AS Attendance2NeedMetIndividualStatus,

    -- NEW: Keeping Children Safe CSC Need Met Family Status
    CASE
       WHEN GM.MinNeedMetInGroup IS NULL THEN NULL
       WHEN GM.MinNeedMetInGroup > 0 THEN 'Pass'
       ELSE 'Fail'
    END AS KeepingChildrenSafeCSCNeedMetFamilyStatus

FROM cdm.Education_Attendance_NeedsMet_Summary_Detail EA
LEFT JOIN GroupMin GM
    ON EA.FamilyID = GM.FamilyID;
""")

OverwriteLoad(
    df,
    'Tables/cdm/vw_individual_attendance_pass_fail',
    'cdm.vw_individual_attendance_pass_fail'
)


# In[22]:


df = spark.sql("""
SELECT
    FamilyID,
    -- For each attendance check, if any record is Fail, then the group flag is Fail.
    CASE 
        WHEN COUNT(CASE WHEN Attendance1NeedStatus = 'Fail' THEN 1 END) > 0 THEN 'Fail'
        ELSE 'Pass'
    END AS Family_Attendance1Need,
    
    CASE 
        WHEN COUNT(CASE WHEN Attendance1NeedMetIndividualStatus = 'Fail' THEN 1 END) > 0 THEN 'Fail'
        ELSE 'Pass'
    END AS Family_Attendance1NeedMetIndividual,
    
    CASE 
        WHEN COUNT(CASE WHEN Attendance2NeedStatus = 'Fail' THEN 1 END) > 0 THEN 'Fail'
        ELSE 'Pass'
    END AS Family_Attendance2Need,
    
    CASE 
        WHEN COUNT(CASE WHEN Attendance2NeedMetIndividualStatus = 'Fail' THEN 1 END) > 0 THEN 'Fail'
        ELSE 'Pass'
    END AS Family_Attendance2NeedMetIndividual,

	    CASE 
        WHEN COUNT(CASE WHEN KeepingChildrenSafeCSCNeedMetFamilyStatus = 'Fail' THEN 1 END) > 0 THEN 'Fail'
        ELSE 'Pass'
    END AS KeepingChildrenSafeCSCNeedMetFamilyStatus,
    
    -- Overall family status: if any individual fails any attendance check, then the overall status is Fail.
    CASE 
        WHEN COUNT(CASE WHEN Attendance1NeedStatus = 'Fail' THEN 1 END) > 0
          OR COUNT(CASE WHEN Attendance2NeedStatus = 'Fail' THEN 1 END) > 0
         -- OR COUNT(CASE WHEN Attendance2NeedMetIndividualStatus = 'Fail' THEN 1 END) > 0
		  OR COUNT(CASE WHEN KeepingChildrenSafeCSCNeedMetFamilyStatus = 'Fail' THEN 1 END) > 0
        THEN 'Fail'
        ELSE 'Pass'
    END AS FamilyStatus

FROM cdm.vw_individual_attendance_pass_fail
GROUP BY FamilyID
Order by FamilyID

""")

OverwriteLoad(
    df,
    'Tables/cdm/vw_individual_attendance_pass_fail_Summary',
    'cdm.vw_individual_attendance_pass_fail_Summary'
)


# In[23]:


df = spark.sql("""
SELECT 
    FamilyID,
    COUNT(DISTINCT SchoolPersonID) AS ChildrenInFamily
FROM 
    cdm.vw_individual_attendance_pass_fail
WHERE 
    FamilyID IS NOT NULL
GROUP BY 
    FamilyID;
""")

OverwriteLoad(
    df,
    'Tables/cdm/vw_family_children_counts',
    'cdm.vw_family_children_counts'
)


# In[17]:


df = spark.sql("""
SELECT *
FROM (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY UPN ORDER BY SFStartDate) AS RowNum
    FROM cdm.education_attendance_calculations
) RankedRows
WHERE RowNum = 1;
""")

OverwriteLoad(
    df,
    'Tables/cdm/education_attendance',
    'cdm.education_attendance'
)


# In[38]:


df = spark.sql("""
 SELECT *
FROM (VALUES
    ('G', 'Family holiday (not agreed)', 'Unauthorised Absence', 'Out for whole session'),
    ('N', 'No reason yet provided for absence', 'Unauthorised Absence', 'Out for whole session'),
    ('O', 'Unauthorised Abs', 'Unauthorised Absence', 'Out for whole session'),
    ('U', 'Late (after registers closed)', 'Unauthorised Absence', 'Out for whole session'),
    ('/', 'Present (AM)', 'Present', 'In for whole session'),
    ('\', 'Present (PM)', 'Present', 'In for whole session'),
    ('B', 'Education off site (no Dual reg)', 'Approved Education Activity', 'Out for whole session'),
    ('C', 'Other authorised circumstances', 'Authorised Absence', 'Out for whole session'),
    ('D', 'Dual registration', 'Approved Education Activity', 'Out for whole session'),
    ('E', 'Excluded', 'Authorised Absence', 'Out for whole session'),
    ('F', 'Extended family holiday (agreed)', 'Authorised Absence', 'Out for whole session'),
    ('H', 'Family holiday (agreed)', 'Authorised Absence', 'Out for whole session'),
    ('I', 'Illness', 'Authorised Absence', 'Out for whole session'),
    ('J', 'Interview', 'Approved Education Activity', 'Out for whole session'),
    ('L', 'Late (before registers closed)', 'Present', 'Late for session'),
    ('M', 'Medical/Dental appointments', 'Authorised Absence', 'Out for whole session'),
    ('P', 'Approved sporting activity', 'Approved Education Activity', 'In for whole session'),
    ('R', 'Religious observance', 'Authorised Absence', 'Out for whole session'),
    ('S', 'Study leave', 'Authorised Absence', 'Out for whole session'),
    ('T', 'Traveller absence', 'Authorised Absence', 'Out for whole session'),
    ('V', 'Educational visit or trip', 'Approved Education Activity', 'Out for whole session'),
    ('W', 'Work experience', 'Approved Education Activity', 'Out for whole session'),
    ('#', 'School closed to pupils & staff', 'Attendance not required', 'Out for whole session'),
    ('Y', 'Enforced closure', 'Attendance not required', 'Out for whole session'),
    ('X', 'Non-compulsory school age absence', 'Attendance not required', 'Out for whole session'),
    ('Z', 'Pupil not on roll', 'Attendance not required', 'Out for whole session'),
    ('-', 'All should attend/No mark recorded', 'No mark', 'Out for whole session')
) AS AttendanceDetails ([Codes], [Description], [Meaning], [Physical Meaning]);   
""")

OverwriteLoad(
    df,
    'Tables/cdm/attendance_session_codes',
    'cdm.attendance_session_codes'
)


# In[3]:





# In[5]:


df = spark.sql("""
SELECT COUNT(*) AS match_termkey_only
FROM (SELECT DISTINCT CAST(TermKey AS STRING) AS TermKey FROM cdm.vw_school_event WHERE TermKey IS NOT NULL) e
JOIN (SELECT DISTINCT CAST(TermKey AS STRING) AS TermKey FROM cdm.vw_school_term_dates WHERE TermKey IS NOT NULL) t
  ON e.TermKey = t.TermKey;
""").show()

