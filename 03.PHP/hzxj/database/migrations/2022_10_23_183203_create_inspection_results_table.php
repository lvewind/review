<?php

use Illuminate\Support\Facades\Schema;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class CreateInspectionResultsTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('inspection_results', function (Blueprint $table) {
            $table->increments('id');
            $table->string('name')->default('');
            $table->integer('inspection_status');
            $table->integer('department_id');
            $table->integer('place_id');
            $table->integer('scheduling_id');
            $table->integer('checked')->default(0);
            $table->string('inspector')->default('');
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
        Schema::dropIfExists('inspection_results');
    }
}
