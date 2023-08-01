/*
  Warnings:

  - Made the column `email` on table `Session` required. This step will fail if there are existing NULL values in that column.

*/
-- AlterTable
ALTER TABLE "Session" ALTER COLUMN "email" SET NOT NULL,
ALTER COLUMN "email" SET DEFAULT '';
