/*
  Warnings:

  - A unique constraint covering the columns `[rocketreachId]` on the table `Person` will be added. If there are existing duplicate values, this will fail.
  - Changed the type of `rocketreachId` on the `Company` table. No cast exists, the column would be dropped and recreated, which cannot be done if there is data, since the column is required.
  - Changed the type of `rocketreachId` on the `Person` table. No cast exists, the column would be dropped and recreated, which cannot be done if there is data, since the column is required.

*/
-- AlterTable
ALTER TABLE "Company" DROP COLUMN "rocketreachId",
ADD COLUMN     "rocketreachId" INTEGER NOT NULL;

-- AlterTable
ALTER TABLE "Person" DROP COLUMN "rocketreachId",
ADD COLUMN     "rocketreachId" INTEGER NOT NULL;

-- CreateIndex
CREATE UNIQUE INDEX "Company_rocketreachId_key" ON "Company"("rocketreachId");

-- CreateIndex
CREATE UNIQUE INDEX "Person_rocketreachId_key" ON "Person"("rocketreachId");
