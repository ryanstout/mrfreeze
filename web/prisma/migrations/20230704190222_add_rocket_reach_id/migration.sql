/*
  Warnings:

  - Added the required column `rocketreachId` to the `Company` table without a default value. This is not possible if the table is not empty.
  - Added the required column `rocketreachId` to the `Person` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE "Company" ADD COLUMN     "rocketreachId" TEXT NOT NULL;

-- AlterTable
ALTER TABLE "Person" ADD COLUMN     "rocketreachId" TEXT NOT NULL;
