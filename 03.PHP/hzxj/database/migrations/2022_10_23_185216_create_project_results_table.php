<?php

use Illuminate\Support\Facades\Schema;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class CreateProjectResultsTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('project_results', function (Blueprint $table) {
            $table->increments('id');
            $table->string('name')->default('');
            $table->integer('inspection_result_id');
            $table->dateTime('inspection_datetime');
            $table->string('project_status')->default('');
            $table->string('photo_url')->nullable();
            $table->string('video_url')->nullable();
            $table->string('photo_path')->nullable();
            $table->string('video_path')->nullable();
            $table->string('note')->nullable();
            $table->timestamps();
            $table->softDeletes();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('project_results');
    }
}
