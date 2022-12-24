using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace DbMigrator.Migrations
{
    /// <inheritdoc />
    public partial class AddedReferences : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AddColumn<int>(
                name: "UserSettingsId",
                table: "Users",
                type: "integer",
                nullable: false,
                defaultValue: 0);

            migrationBuilder.AddColumn<int>(
                name: "UserId",
                table: "UserLinks",
                type: "integer",
                nullable: false,
                defaultValue: 0);

            migrationBuilder.AddColumn<int>(
                name: "LinkPriceHistoryId",
                table: "Links",
                type: "integer",
                nullable: false,
                defaultValue: 0);

            migrationBuilder.CreateIndex(
                name: "IX_Users_UserSettingsId",
                table: "Users",
                column: "UserSettingsId");

            migrationBuilder.CreateIndex(
                name: "IX_UserLinks_LinkId",
                table: "UserLinks",
                column: "LinkId");

            migrationBuilder.CreateIndex(
                name: "IX_UserLinks_UserId",
                table: "UserLinks",
                column: "UserId");

            migrationBuilder.CreateIndex(
                name: "IX_Links_LinkPriceHistoryId",
                table: "Links",
                column: "LinkPriceHistoryId");

            migrationBuilder.AddForeignKey(
                name: "FK_Links_LinkPriceHistory_LinkPriceHistoryId",
                table: "Links",
                column: "LinkPriceHistoryId",
                principalTable: "LinkPriceHistory",
                principalColumn: "Id",
                onDelete: ReferentialAction.Cascade);

            migrationBuilder.AddForeignKey(
                name: "FK_UserLinks_Links_LinkId",
                table: "UserLinks",
                column: "LinkId",
                principalTable: "Links",
                principalColumn: "Id",
                onDelete: ReferentialAction.Cascade);

            migrationBuilder.AddForeignKey(
                name: "FK_UserLinks_Users_UserId",
                table: "UserLinks",
                column: "UserId",
                principalTable: "Users",
                principalColumn: "Id",
                onDelete: ReferentialAction.Cascade);

            migrationBuilder.AddForeignKey(
                name: "FK_Users_UserSettings_UserSettingsId",
                table: "Users",
                column: "UserSettingsId",
                principalTable: "UserSettings",
                principalColumn: "Id",
                onDelete: ReferentialAction.Cascade);
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_Links_LinkPriceHistory_LinkPriceHistoryId",
                table: "Links");

            migrationBuilder.DropForeignKey(
                name: "FK_UserLinks_Links_LinkId",
                table: "UserLinks");

            migrationBuilder.DropForeignKey(
                name: "FK_UserLinks_Users_UserId",
                table: "UserLinks");

            migrationBuilder.DropForeignKey(
                name: "FK_Users_UserSettings_UserSettingsId",
                table: "Users");

            migrationBuilder.DropIndex(
                name: "IX_Users_UserSettingsId",
                table: "Users");

            migrationBuilder.DropIndex(
                name: "IX_UserLinks_LinkId",
                table: "UserLinks");

            migrationBuilder.DropIndex(
                name: "IX_UserLinks_UserId",
                table: "UserLinks");

            migrationBuilder.DropIndex(
                name: "IX_Links_LinkPriceHistoryId",
                table: "Links");

            migrationBuilder.DropColumn(
                name: "UserSettingsId",
                table: "Users");

            migrationBuilder.DropColumn(
                name: "UserId",
                table: "UserLinks");

            migrationBuilder.DropColumn(
                name: "LinkPriceHistoryId",
                table: "Links");
        }
    }
}
