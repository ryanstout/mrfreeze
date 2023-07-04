/*
  Warnings:

  - A unique constraint covering the columns `[companyId,sessionId,personId]` on the table `CompanyPerson` will be added. If there are existing duplicate values, this will fail.
  - Added the required column `sessionId` to the `CompanyPerson` table without a default value. This is not possible if the table is not empty.

*/
-- DropIndex
DROP INDEX "CompanyPerson_companyId_personId_key";

-- AlterTable
ALTER TABLE "CompanyPerson" ADD COLUMN     "sessionId" TEXT NOT NULL;

-- CreateIndex
CREATE UNIQUE INDEX "CompanyPerson_companyId_sessionId_personId_key" ON "CompanyPerson"("companyId", "sessionId", "personId");
