/*
  Warnings:

  - A unique constraint covering the columns `[rocketreachId]` on the table `Company` will be added. If there are existing duplicate values, this will fail.

*/
-- DropIndex
DROP INDEX "rocketreachId";

-- CreateIndex
CREATE UNIQUE INDEX "Company_rocketreachId_key" ON "Company"("rocketreachId");
