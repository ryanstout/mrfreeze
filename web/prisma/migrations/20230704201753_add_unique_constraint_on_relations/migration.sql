/*
  Warnings:

  - A unique constraint covering the columns `[companyId,personId]` on the table `CompanyPerson` will be added. If there are existing duplicate values, this will fail.
  - A unique constraint covering the columns `[sessionId,companyId]` on the table `SessionCompany` will be added. If there are existing duplicate values, this will fail.
  - A unique constraint covering the columns `[sessionId,personId]` on the table `SessionPerson` will be added. If there are existing duplicate values, this will fail.

*/
-- CreateIndex
CREATE UNIQUE INDEX "CompanyPerson_companyId_personId_key" ON "CompanyPerson"("companyId", "personId");

-- CreateIndex
CREATE UNIQUE INDEX "SessionCompany_sessionId_companyId_key" ON "SessionCompany"("sessionId", "companyId");

-- CreateIndex
CREATE UNIQUE INDEX "SessionPerson_sessionId_personId_key" ON "SessionPerson"("sessionId", "personId");
