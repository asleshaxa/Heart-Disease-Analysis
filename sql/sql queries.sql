
USE csvdb;
select * from heart_new2;
select HeartDisease, Diabetic from heart_new2;
select * from heart_new2 order by AgeCategory;

SELECT COUNT(*) AS Total_Patients
FROM heart_new2;

SELECT HeartDisease, COUNT(*) AS Count
FROM heart_new2
GROUP BY HeartDisease;

SELECT Smoking, HeartDisease, COUNT(*) AS Count
FROM heart_new2
GROUP BY Smoking, HeartDisease;